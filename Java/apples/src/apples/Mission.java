/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package apples;

/**
 *
 * @author Nick Marriotti
 */
public class Mission {
    String name;
    String date;
    String area;
    String FMC;
    int signalCount = 0;
    
    public void setName(String s) {
        this.name = s;
    }
    
    public void setDate(String d) {
        this.date = d;
    }
    
    public void setArea(String a) {
        this.area = a;
    }
    
    public void setFMC(String c) {
        this.FMC = c;
    }
    
    public void setSignalCount() {
        this.signalCount+= 1;
    }
    
    public int getSignalCount() {
        return signalCount;
    }
    
    public String getName() {
        return name;
    }
    
    public String getDate() {
        return date;
    }
    
    public String getArea() {
        return area;
    }
    
    public String getFMC() {
        return FMC;
    }
    
}
