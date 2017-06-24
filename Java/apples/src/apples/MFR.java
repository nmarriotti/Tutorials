/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package apples;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.GridBagLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.LineNumberReader;
import java.util.ArrayList;
import java.util.List;
import javax.swing.Box;
import javax.swing.BoxLayout;
import javax.swing.DefaultListModel;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JToolBar;
import javax.swing.ScrollPaneConstants;
import javax.swing.filechooser.FileNameExtensionFilter;

/**
 *
 * @author Nick
 */
public class MFR extends JFrame {
    
    JToolBar tb, tbSouth;
    ImageIcon open, remove, startIcon, saveIcon;
    JButton btnOpen, btnRemove, btnStart, btnSave;
    JFileChooser saveFiles;
    JList listbox;
    JPanel mainPanel, panel1, buttonPanel;
    JScrollPane scroller, scroller2;
    JLabel listLabel, status;
    JTextArea textArea;
    JFileChooser browseFiles;
    DefaultListModel listModel;
    JOptionPane Dialog1;
    JDialog dialog;
    String missionName, area, FMC, msnDate = null;
    List<Mission> missionList = new ArrayList<Mission>();
    List<Signal> signalArray = new ArrayList<Signal>();
    int errorsFound = 0;
    int signalCount = 1;
    int arrayPos = 0;
    int lineNumber = 0;
    boolean GoodToGo = true;
    
    // Constructor
    public MFR() {
        
        // Set Window Title
        super("MFR Generator");

        // Set sont for JTextArea
        Font CourierNew = new Font("Courier New", Font.PLAIN, 18);
        
        // Add the text area
        textArea = new JTextArea();
        scroller2 = new JScrollPane(textArea);
        scroller2.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
        add(scroller2);
        
        // Change font in text area
        textArea.setFont(CourierNew);
        
        // Set message in text area
        textArea.setText("Load mission files and click process...");
        
        mainPanel = new JPanel();
        mainPanel.setLayout(new BoxLayout(mainPanel, BoxLayout.Y_AXIS));
        
        // Add top toolbar
        tb = new JToolBar();
        tb.setFloatable(false);
        add(tb, BorderLayout.NORTH);
        
        // Add bottom toolbar
        tbSouth = new JToolBar();
        tbSouth.setFloatable(false);
        add(tbSouth, BorderLayout.SOUTH);
        status = new JLabel();
        status.setText("Load mission files and click Process");
        tbSouth.add(status);
        
        // Open button
        open = new ImageIcon("images/openFile.png");
        btnOpen = new JButton(open);
        tb.add(btnOpen);

        // Remove file button
        remove = new ImageIcon("images/remove.png");
        btnRemove = new JButton(remove);
        
        // Start button
        startIcon = new ImageIcon("images/start.png");
        btnStart = new JButton(startIcon);
        btnStart.setEnabled(false);
        
        // Save button
        saveIcon = new ImageIcon("images/save_big.png");
        btnSave = new JButton(saveIcon);
        btnSave.setBorderPainted(true);
        btnSave.setEnabled(false);
        
        // Create listbox and model to hold values
        listModel = new DefaultListModel();
        listbox = new JList(listModel);
        listbox.setPreferredSize(new Dimension(200, 200));
        
        // Add scrollbar to listbox
        scroller = new JScrollPane(listbox);
        scroller.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_AS_NEEDED);
        
        this.getContentPane().add(BorderLayout.EAST, mainPanel);
        
        listLabel = new JLabel("Missions Selected");
        scroller.setPreferredSize(new Dimension(250,120));
        panel1 = new JPanel();
        panel1.add(scroller);
        mainPanel.add(panel1);
        mainPanel.add(btnSave);
        
        // Add buttons to top toolbar
        tb.add(btnOpen);
        tb.add(btnRemove); 
        tb.add(btnStart);
        
        //Add actionHandler to buttons
        theHandler handler = new theHandler();
        btnOpen.addActionListener(handler);
        btnRemove.addActionListener(handler);  
        btnStart.addActionListener(handler);
        btnSave.addActionListener(handler);
    }
    
    private class theHandler implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            if(event.getSource() == btnOpen) {
                //Bring up open files
                browseFiles();
            }
        
            if(event.getSource() == btnSave) {
                //Bring up save dialog
                Save();
            }
            
            if(event.getSource() == btnStart) {
                // Start parsing and generating
                for(int i=0; i<listModel.getSize(); i++) {
                    parseCSV((String)listModel.get(i));
                }
                
                if(GoodToGo == true) {
                    ReadyToParseDialog();  
                } else {
                    JOptionPane.showMessageDialog(dialog, "An unknown error occurred!", "Error", JOptionPane.ERROR_MESSAGE);                    
                }

            }
            
            if(event.getSource() == btnRemove) {
                // Remove selected file from the listbox
                if(listbox.getSelectedIndex() > -1) {
                    removeFile(listbox.getSelectedIndex());
                } else {
                    JOptionPane.showMessageDialog(dialog, "No mission selected!", "Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        }
    }
    
    public void showErrorDialog(String input, boolean hasSDF, boolean hasFreq, boolean hasDate, boolean hasTime, boolean hasSOI) {
        //Ask if the user wants to exit the program
        textArea.setText("Unable to process file. Correct the errors and try again...");
        status.setText("Error found!");
        Object[] options = {"Ok"};
        int n = JOptionPane.showOptionDialog(this,"Filename does not contain all required information! Unable to continue. \n" + input + "\n\n SDF: " + hasSDF + "\n Frequency: " + hasFreq + "\n Date: " + hasDate + "\n Time: " + hasTime + "\n Analyzed: " + hasSOI + "\n\nItems that show false were not found and must be fixed.\nIt is ok if SDF was false.", "Error",
        JOptionPane.OK_OPTION,
        JOptionPane.ERROR_MESSAGE,
        null,
        options,
        options[0]);
    }

    public void ReadyToParseDialog() {
        //Ask if the user wants to exit the program
        Object[] options = {"Yes",
                            "No"};
        int n = JOptionPane.showOptionDialog(this,"Missions parsed successfully! Ready to generage MFR?", "Continue",
        JOptionPane.YES_NO_OPTION,
        JOptionPane.QUESTION_MESSAGE,
        null,
        options,
        options[1]);
        
        // Check if YES was clicked and close the app
        if (n == JOptionPane.YES_OPTION) {
            // Generate MFR
            //textArea.append("\nOutput FMR now...");
            textArea.setText("Total filenames processed: " + signalArray.size());
            textArea.append("\n============================");
            for(int i=0; i<missionList.size(); i++) {
                GenerateMFR(i);
            }
            
        }
    }
    
    void GenerateMFR(int i) {
        int signalCount = 0;
        String currSignal, currMission = null;
        ArrayList<String> completed = new ArrayList<String>();
        
        // Set mission name
        currMission = missionList.get(i).getName();
        
        // Output the mission name, date and area
        textArea.append("\n" + missionList.get(i).getName() + " - " + missionList.get(i).getDate() + " - " + missionList.get(i).getArea());
        for(int x=0; x<signalArray.size(); x++) {
            // Signal is apart of current mission and the filename has not been completed yet
            if(signalArray.get(x).getMission().equals(missionList.get(i).getName()) && !completed.contains(signalArray.get(x).getFilename())) {
                // Set the current signal
                currSignal = signalArray.get(x).getSDFSOI();                   
                // Start outputting the total for each mission
                for(int y=0; y<signalArray.size(); y++) {
                    if(signalArray.get(y).getSDFSOI().equals(currSignal) && signalArray.get(y).getMission().equals(currMission) && !completed.contains(signalArray.get(y).getFilename())) {
                        // It is the same signal. Increment count and mark completed
                        signalCount++;
                        completed.add(signalArray.get(y).getFilename());
                    }
                }
                // Output the total
                textArea.append("\n" + signalArray.get(x).getAnalyzedSOI() + "/" + signalArray.get(x).getSDF() + "/" + signalCount);
                signalCount = 0;         
            }
        }
        
        // Set signal count to 0 and remove all completed signals
        signalCount = 0;
        completed.clear();
        btnSave.setEnabled(true);
    }
    
    void browseFiles() {
        browseFiles = new JFileChooser();
        FileNameExtensionFilter txtType = new FileNameExtensionFilter("Comma Delimited (.csv)", "csv");
        browseFiles.addChoosableFileFilter(txtType);
        int result = browseFiles.showOpenDialog(this);
        if (result == JFileChooser.APPROVE_OPTION) {
            // user selects a file
            File selectedFile = browseFiles.getSelectedFile();
            // Check if file is a .csv
            if(getFileExtension(selectedFile).equals("csv")) {
                // Load filename into textbox
                if(checkFileExists(selectedFile.getAbsolutePath()) && !listModel.contains(selectedFile.getAbsolutePath())) {
                    //add file to JList
                    btnStart.setEnabled(true);
                    listModel.addElement(selectedFile.getAbsolutePath());
                    status.setText(selectedFile + " added!");
                } else {
                    // File does not exist
                    JOptionPane.showMessageDialog(dialog, "Mission does not exist or is already added!", "Error", JOptionPane.ERROR_MESSAGE);                
                }
            } else {
                // File is not .csv
                JOptionPane.showMessageDialog(dialog, "File type not supported!", "Error", JOptionPane.ERROR_MESSAGE);
            }
        }
    }
    
        public void parseCSV(String fpath) {  
        //Count the number of lines in the file
        try {
            FileReader fr = new FileReader(fpath);
            LineNumberReader lnr = new LineNumberReader(fr);
               
            //Count each line until it reaches a blank line
            while(lnr.readLine() != null) {
                lineNumber++;
            }
        
        } catch(IOException e){
            e.printStackTrace();
    	}
        
        System.out.println("Lines: " + lineNumber);
        
        String line = "";
        String cvsSplitBy = ",";

        try (BufferedReader br = new BufferedReader(new FileReader(fpath))) {
            
            //Set current line to 1
            int currentLine = 1;
            
            
            while ((line = br.readLine()) != null) {
                //Remove quotes from line
                line = line.replace("\"", "");
                
                //Split into array where there is a comma
                String[] info = line.split(cvsSplitBy);
                
                //load the mission details into an array and set variables
                if (currentLine == 1) {
                    //textArea.setText(Arrays.toString(info) + "\n");
                    missionName = info[0];
                    area = info[2];
                    msnDate = info[1];
                    FMC = info[3];
                    System.out.println(missionName + " " + msnDate + " " + area + " " + FMC);
                    
                    // Create a new mission and load values
                    Mission mission = new Mission();
                    mission.setName(missionName);
                    mission.setDate(msnDate);
                    mission.setArea(area);
                    mission.setFMC(FMC);
                    
                    // Create ArrayList and add mission
                    missionList.add(mission);
                    
                    // Check if values are set
                    System.out.println(mission.getName());
                }
                else if(currentLine >= 3) {
                    //textArea.append(Arrays.toString(info) + "\n");
                 
                    // Process the first signal
                    Signal signal = new Signal();
                    signalArray.add(signal);
                    signalArray.get(arrayPos).setMission(missionName);
                    signalArray.get(arrayPos).setFilename(info[0]);
                    
                    // Set the analyzed SOI
                    signalArray.get(arrayPos).setAnalyzedSOI(info[1]);                    
                    if(signalArray.get(arrayPos).getAnalyzedSOI().equals("")) {
                        // There is no SOI
                        signalArray.get(arrayPos).hasError = true;
                    }

                    
                    signalArray.get(arrayPos).Parse();
                    System.out.println(signalArray.get(arrayPos).getTime());
                    if(signalArray.get(arrayPos).hasError == true) {
                        GoodToGo = false;
                        showErrorDialog(signalArray.get(arrayPos).getFilename(), signalArray.get(arrayPos).hasSDF, signalArray.get(arrayPos).hasFreq, signalArray.get(arrayPos).hasDate, signalArray.get(arrayPos).hasTime, signalArray.get(arrayPos).hasSOI);
                        break;
                    }
                    arrayPos++;
                    signalCount++;
                    
                }
                //increment the current line
                missionList.get(0).setSignalCount();
                currentLine++;
                
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
        
        if(GoodToGo == true) {
            status.setText("Processed " + lineNumber + " line(s) successfully!");
        }
    }

    private String getFileExtension(File file) {
        String name = file.getName();
        try {
            return name.substring(name.lastIndexOf(".") + 1);
        } catch (Exception e) {
            return "";
        }
    }
    
    void removeFile(int s) {
        status.setText(listModel.get(s).toString() + " removed!");
        listModel.remove(s);    
        if(listModel.getSize() == 0) {
            btnStart.setEnabled(false);
        }
    }

    boolean checkFileExists(String fpath) {
        File f = new File(fpath);
        if(f.exists() && !f.isDirectory()) {
            return true;
        } else {
            return false;
        }
    }    
    
    void Save() {
        saveFiles = new JFileChooser();
        FileNameExtensionFilter txtType = new FileNameExtensionFilter("Text (.txt)", "txt");
        saveFiles.addChoosableFileFilter(txtType);
        try {
            File file = new File("fileName.txt");
            int r = saveFiles.showSaveDialog(this);   
            if(r == JFileChooser.APPROVE_OPTION)
            {   
                FileWriter writer = new FileWriter(saveFiles.getSelectedFile());  
                textArea.write(writer);
                writer.flush();
                writer.close();
                System.out.println("File saved.");
                status.setText(saveFiles.getSelectedFile() + " saved!");
            }
            else if(r == JFileChooser.CANCEL_OPTION) {
                System.out.println("Do nothing for CANCEL");
            }
        } catch (Exception ex) {
            JOptionPane.showMessageDialog(null, "File could not be written, try again.");
        }     
    }
    
    
}
