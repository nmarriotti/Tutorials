/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package apples;
import javax.swing.JFrame;

public class Apples {

    public static void main(String[] args) {
        Menu window2 = new Menu();
        window2.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        window2.setSize(200,250);
        window2.setResizable(false);
        window2.setVisible(true);
    }
    
}
