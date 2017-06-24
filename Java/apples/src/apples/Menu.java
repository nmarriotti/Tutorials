/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package apples;

import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.BoxLayout;
import javax.swing.Icon;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;

/**
 *
 * @author Nick
 */
public class Menu extends JFrame {
    
    JButton FMR, MFR;
    JLabel message, message2, iconPlaceHolder;
    ImageIcon report;
    
    public Menu() {
        //Set Layout
        super("Main Menu");
        setLayout(new FlowLayout());
        
        //Display the main menu icon
        report = new ImageIcon("images/report.png");
        iconPlaceHolder = new JLabel((Icon) report);
        add(iconPlaceHolder);
        
        FMR = new JButton("Final Mission Report"); 
        FMR.setMargin(new Insets(5,5,10,10));
        add(FMR);
        
        MFR = new JButton("Monthly Feedback Report");
        MFR.setMargin(new Insets(5,5,10,10));
        add(MFR);

        message2 = new JLabel(" v1.0 - CTR1 Marriotti");
        add(message2);
        
        //Add action listeners
        theHandler handler = new theHandler();
        FMR.addActionListener(handler);
        MFR.addActionListener(handler);    
    }
    
    private class theHandler implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            if(event.getSource() == FMR) {
                // Open FMR Window
                Toolbar FMR_window = new Toolbar();
                FMR_window.setSize(500,600);
                FMR_window.setResizable(false);
                FMR_window.setVisible(true);
            }
            
            if(event.getSource() == MFR) {
                // Open MFR Window
                MFR MFR_window = new MFR();
                MFR_window.setSize(800,800);
                MFR_window.setResizable(false);
                MFR_window.setVisible(true);
                
            }
        }
    }
}
