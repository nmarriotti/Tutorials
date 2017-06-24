/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package apples;
import java.awt.FlowLayout;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;
import javax.swing.JFrame;
import javax.swing.JTextField;
import javax.swing.JPasswordField;
import javax.swing.JOptionPane;
import javax.swing.JButton;

public class EventHandler extends JFrame {
    
    private JTextField item1;
    private JTextField item2;
    private JTextField item3;
    private JPasswordField passwordField;
    private JButton item4, item5;
    private Toolbar tb;
    
    public EventHandler() {
        super("The title goes here");
        setLayout(new FlowLayout());
        
        item1 = new JTextField(10);
        add(item1);
        
        item2 = new JTextField("Enter text here");
        add(item2);
        
        item3 = new JTextField("uneditable", 20);
        item3.setEditable(false);
        add(item3);
        
        passwordField = new JPasswordField(20);
        add(passwordField);
        
        item4 = new JButton("Button");
        add(item4);
        
        item5 = new JButton("Toolbar Example");
        add(item5);
        
        theHandler handler = new theHandler();
        item1.addActionListener(handler);
        item2.addActionListener(handler);
        item3.addActionListener(handler);
        passwordField.addActionListener(handler);
        item4.addActionListener(handler);
        item5.addActionListener(handler);

    }
    
    private class theHandler implements ActionListener {
        public void actionPerformed(ActionEvent event) {
            String string = "";
            
            if(event.getSource() != item4 && event.getSource() != item5) {
                if(event.getSource() == item1)
                    string = String.format("Field 1 : %s", event.getActionCommand());
                else if(event.getSource() == item2)
                    string = String.format("Field 2 : %s", event.getActionCommand());
                else if(event.getSource() == item3)
                    string = String.format("Field 3 : %s", event.getActionCommand());
                else if(event.getSource() == passwordField)
                    string = String.format("Psssword : %s", event.getActionCommand());
                
                JOptionPane.showMessageDialog(null, string);  
                
            } else if(event.getSource() == item5) {             
                    tb = new Toolbar();
                    tb.setSize(400,400);
                    tb.setVisible(true);
            } 
        }
    }   
}
