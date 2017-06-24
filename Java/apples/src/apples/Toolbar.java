package apples;
import java.awt.BorderLayout;
import java.awt.Font;
import java.awt.GraphicsDevice;
import java.awt.Toolkit;
import java.awt.Window;
import javax.swing.*;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileFilter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.LineNumberReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.filechooser.FileNameExtensionFilter;

public class Toolbar extends JFrame {
    
    /* Define variables */
    JToolBar tb, tbSouth;
    JButton exit, loadCSV, fullScreen, open, save;
    ImageIcon exitIcon, submitIcon, iconFullScreen, iconFileChooser, iconSave;
    JTextField filename;
    JTextArea textArea;
    JLabel status;
    boolean isMaximized;
    JFileChooser browseFiles, saveFiles;
    String missionName, area, FMC, msnDate = null;
    List<Mission> missionList = new ArrayList<Mission>();
    List<Signal> signalArray = new ArrayList<Signal>();
    int errorsFound = 0;
    int signalCount = 1;
    int arrayPos = 0;
    int lineNumber = 0;

    public Toolbar() {
        
        // Set sont for JTextArea
        Font CourierNew = new Font("Courier New", Font.PLAIN, 14);
        
        try {
            setUIFont(new javax.swing.plaf.FontUIResource("Arial",Font.BOLD,12));    
        }
        catch(Exception e){}
        
        isMaximized = false;
        
        setSize(400,400);
        setTitle("Java FMR - CTR1 Marriotti");
        
        /* Create a toolbar object */
        tb = new JToolBar();
        tbSouth = new JToolBar();
        
        /* Create a button with an image and tooltip */
        exitIcon = new ImageIcon("images/exit.png");
        exit = new JButton(exitIcon);
        exit.setToolTipText("Exit");
        
        /* Create a button with an image and tooltip */
        iconSave = new ImageIcon("images/save.png");
        save = new JButton(iconSave);
        save.setToolTipText("Save");
        tbSouth.add(save);
        save.setEnabled(false);
        
        /* Create fullscreen button */
        iconFullScreen = new ImageIcon("images/fullscreen.png");
        fullScreen = new JButton(iconFullScreen);
        fullScreen.setToolTipText("Fullscreen");
        
        /* Add the buttons to the toolbar */
        tb.add(exit);
        tb.add(fullScreen);
        
        /* Lock the toolbar in place at the top of the window */
        tb.setFloatable(false);
        add(tb, BorderLayout.NORTH);
        
        /* Add toolbar at the bottom of window */
        tbSouth.setFloatable(false);
        add(tbSouth, BorderLayout.SOUTH);
        
        /*Add Label to bottom toolbar */
        status = new JLabel();
        tbSouth.add(status);
        
        /* Create a textbox */
        filename = new JTextField(10);
        filename.setEditable(false);
        tb.add(filename);
        
        /* Create a file chooser */
        iconFileChooser = new ImageIcon("images/open.png");
        open = new JButton(iconFileChooser);
        open.setToolTipText("Exit");
        tb.add(open);
        
        /* Create load csv button and add to toolbar */
        submitIcon = new ImageIcon("images/submit.png");
        loadCSV = new JButton(submitIcon);
        loadCSV.setToolTipText("Load and parse CSV from filename");
        loadCSV.setEnabled(false);
        tb.add(loadCSV);
        
        /* Add textarea */
        textArea = new JTextArea();
        textArea.setFont(CourierNew);
        JScrollPane scrollPane = new JScrollPane(textArea);
        textArea.setEditable(true);
        textArea.setText("Load a CSV file and click the green button to process...");
        
        // Add scroll bar to text area
        scrollPane.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
        scrollPane.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
        add(scrollPane);
        
        /* Add an event handler to the buttons */       
        Handler theHandler = new Handler();
        save.addActionListener(theHandler);
        exit.addActionListener(theHandler);
        loadCSV.addActionListener(theHandler);
        fullScreen.addActionListener(theHandler);
        open.addActionListener(theHandler);
        filename.setText("<Select a file...>");
    }
    
    private class Handler implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            String string = null;
            
            // Check if the user clicked the browse button
            if(event.getSource() == open) {
               browseFiles();
            }
            
            if(event.getSource() == save) {
               Save();
            }
            
            /* Check if the exit button was clicked*/
            else if(event.getSource() == exit) {
                showExitDialog();  
                
            } else if(event.getSource() == loadCSV) {
                
                // Process the CSV
                parseCSV(filename.getText());
                
            }  else if(event.getSource() == fullScreen) {
                maximizeWindow();
            } 
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
    
    void maximizeWindow() {
        if(isMaximized) {
            setExtendedState(JFrame.NORMAL);
            isMaximized = false;
        }
        else {
            setExtendedState(JFrame.MAXIMIZED_BOTH);
            isMaximized = true;
        }
    }
    
    void browseFiles() {
        browseFiles = new JFileChooser();
        FileNameExtensionFilter txtType = new FileNameExtensionFilter("Comma Delimited (.csv)", "csv");
        browseFiles.addChoosableFileFilter(txtType);
        int result = browseFiles.showOpenDialog(this);
        if (result == JFileChooser.APPROVE_OPTION) {
            // user selects a file
            File selectedFile = browseFiles.getSelectedFile();
            // Load filename into textbox
            filename.setText(selectedFile.getAbsolutePath());
            if(checkFileExists(selectedFile.getAbsolutePath())) {
                loadCSV.setEnabled(true);
                status.setText("Ready to parse!");
            } else {
                // File does not exist
                filename.setText(null);
                loadCSV.setEnabled(false);
            }
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
    
    public void showExitDialog() {
        //Ask if the user wants to exit the program
        Object[] options = {"Yes",
                            "No"};
        int n = JOptionPane.showOptionDialog(this,"Are you sure you want to exit?", "Are you sure?",
        JOptionPane.YES_NO_OPTION,
        JOptionPane.QUESTION_MESSAGE,
        null,
        options,
        options[1]);
        
        // Check if YES was clicked and close the app
        if (n == JOptionPane.YES_OPTION) {
            setVisible(false);
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
                        showErrorDialog(signalArray.get(arrayPos).getFilename(), signalArray.get(arrayPos).hasSDF, signalArray.get(arrayPos).hasFreq, signalArray.get(arrayPos).hasDate, signalArray.get(arrayPos).hasTime, signalArray.get(arrayPos).hasSOI );
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
        
        if(signalArray.get(arrayPos-1).hasError == false) {
            outputResults();
            status.setText("Processed " + lineNumber + " line(s) successfully!");
        }
    }
    
    public void outputResults() {
        textArea.setText("Mission: " + missionList.get(0).getName() + "\n");
        textArea.append("Signal files found: " + signalArray.size());
        textArea.append("\nMission processed successfully!\n\n");
        GenerateFMR();
        save.setEnabled(true);
    }
    
    public void GenerateFMR() {
        int count = 1;
        int currSignalCount = 1;
        int i = 0;
        String currSignal = null;
        String nextSignal = null;
        String currSDF = null;
        String currSOI = null;
        String nextSOI = null;
        ArrayList<String> completed = new ArrayList<String>();
        int num = 0;
        
        textArea.append("Final Mission Report\n");
        
        System.out.println("Starting to generate FMR...");
        
        while(completed.size() != signalArray.size()) {
            num = 0;
            currSignal = signalArray.get(i).getFilename();
            
            if(!completed.contains(currSignal)) {
                if(count < 10)
                    textArea.append("  " + count + ".  ");
                else
                    textArea.append(" " + count + ".  ");
            
                //Output the signal
                textArea.append(currSignal+"\n");
            
                //Check for signals with valid SDF
                if(signalArray.get(i).hasSDF) {
                    System.out.println("Looking for signals with valid " + signalArray.get(i).getSDF() + " SDF");
                    if (CheckForValidSDF(signalArray.get(i).getSDF(), signalArray.get(i).getAnalyzedSOI())) {
                        //It is valid. Loop through and look for more
                        try {
                            if(i != signalArray.size()) {
                                for(int x=(i+1); x<signalArray.size(); x++) {
                                    if(!completed.contains(signalArray.get(x).getFilename())) {
                                        if(signalArray.get(x).hasSDF) {
                                            // Check if it was identified as the same signal
                                            if(signalArray.get(x).getAnalyzedSOI().equals(signalArray.get(i).getAnalyzedSOI())) {
                                                // Check if it has valid SDF
                                                if(CheckForValidSDF(signalArray.get(x).getSDF(), signalArray.get(x).getAnalyzedSOI())) {
                                                    // Found another valid SDF. Output it
                                                    System.out.println("Found a signal that matched " + signalArray.get(x).getSDF() + " and " + signalArray.get(x).getAnalyzedSOI());
                                                    textArea.append("      " + signalArray.get(x).getFilename()+"\n");
                                                    // Add the signal to the completed list
                                                    completed.add(signalArray.get(x).getFilename());
                                                    num++;
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        } catch (IndexOutOfBoundsException e) {
                            // Do nothing
                        }
                        
                        if(num>=1)
                            textArea.append("      COMMENT: SOI'S VERIFIED AS " + signalArray.get(i).getAnalyzedSOI() + ".\n");
                        else
                            textArea.append("      COMMENT: SOI VERIFIED AS " + signalArray.get(i).getAnalyzedSOI() + ".\n");
                    
                    } else {
                        //Has SDF but isn't valid
                        //Look for anything that matches the SOI
                        try {
                            if(i != signalArray.size()) {
                                for(int x=(i+1); x<signalArray.size(); x++) {
                                    if(!completed.contains(signalArray.get(x).getFilename())) {
                                        if(signalArray.get(x).getAnalyzedSOI().equals(signalArray.get(i).getAnalyzedSOI())) {
                                            System.out.println("Found a signal that matched " + signalArray.get(x).getAnalyzedSOI());
                                            textArea.append("      " + signalArray.get(x).getFilename()+"\n");
                                            // Add the signal to the completed list
                                            completed.add(signalArray.get(x).getFilename());
                                            num++;                                    
                                        }
                                    }
                                }
                            }
                        } catch(IndexOutOfBoundsException e) {
                            // Do nothing
                        }  
                        if(num>=1)
                            textArea.append("      COMMENT: SOI'S FOUND TO BE " + signalArray.get(i).getAnalyzedSOI() + ".\n");
                        else
                            textArea.append("      COMMENT: SOI FOUND TO BE " + signalArray.get(i).getAnalyzedSOI() + ".\n");                        
                    }
                    
                } else {
                    // Doesnt have SDF.
                    // Just look for other signals that are the same.
                    try {
                        for(int x=(i+1); x<signalArray.size(); x++) {
                            if(!completed.contains(signalArray.get(x).getFilename())) {
                                if(signalArray.get(x).getAnalyzedSOI().equals(signalArray.get(i).getAnalyzedSOI())) {
                                    System.out.println("Found a signal that matched " + signalArray.get(x).getAnalyzedSOI());
                                    textArea.append("      " + signalArray.get(x).getFilename()+"\n");
                                    // Add the signal to the completed list
                                    completed.add(signalArray.get(x).getFilename());
                                    num++;                                    
                                }
                            }
                        }
                    } catch (IndexOutOfBoundsException e) {
                        // Do nothing
                    }
                        if(num>=1)
                            textArea.append("      COMMENT: SOI'S FOUND TO BE " + signalArray.get(i).getAnalyzedSOI() + ".\n");
                        else
                            textArea.append("      COMMENT: SOI FOUND TO BE " + signalArray.get(i).getAnalyzedSOI() + ".\n");                    
                }
                
                completed.add(signalArray.get(i).getFilename());
                count++;
                
            } else {
                i++;
            }
        }
    }
    
    public boolean CheckForValidSDF(String SDF, String SOI) {
        if(SDF.contains(SOI.replace(" ", "")))
            return true;
        else
            return false;
    }
    
    public static void setUIFont(javax.swing.plaf.FontUIResource f)
    {   
        java.util.Enumeration keys = UIManager.getDefaults().keys();
        while(keys.hasMoreElements()) {
            Object key = keys.nextElement();
            Object value = UIManager.get(key);
            if(value instanceof javax.swing.plaf.FontUIResource) 
                UIManager.put(key, f);
        }
    }
}
