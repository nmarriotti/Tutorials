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
public class Signal extends Mission {
    String filename;
    String mission;
    boolean wasAnalyzed;
    boolean hasAnalyst; 
    boolean hasComment;
    boolean hasFreq;
    boolean hasSDF; 
    boolean hasDate; 
    boolean hasTime;
    boolean validSDF;
    boolean hasSOI;
    int i = 0;
    boolean hasError;
    
    String SOI, analyzedSOI, analyst, comment, SDF, time, freq, SDFSOI = null;
    String[] SDFtypes = { "SIG1", "SIG2", "SIG3", "SIG4" };
    String[] freqTypes = { "MHZCENTERED", "CENTERED", "MHZCENT", "MHZCEN", "MHZ" };
    
    // Used to check if all info was found in the filename
    boolean parsed = false;
    
    // Constructor
    public Signal() {
        wasAnalyzed = false;
        hasAnalyst = false;
        hasComment = false;
        hasFreq = false;
        hasSDF = false;
        hasDate = false;
        hasTime = false;
        hasSOI = true;
        hasError = false;
    }
    
    public void setFilename(String f) {
        this.filename = f;
    }
    
    public void setMission(String m) {
        this.mission = m;
    }
    
    // Loop through until all peices of info are found and set
    public void Parse() {
        
        String splitBy = "_";
        String[] chunk = filename.split(splitBy);
        int chunkLength = chunk.length;
        int[] completedChunk;
        
        if(chunkLength>2) {
            while(i <= chunkLength-1) {
                
                //Output current chunk
                System.out.println("[" + i + "] Current chunk: " + chunk[i]);
                
                //Search for the required field
                if (!hasSDF) 
                    try {
                        CheckForSDF(chunk[i], chunk[i+1]);
                    } catch (ArrayIndexOutOfBoundsException e) {
                        //Do nothing
                    }
                if (!hasFreq) 
                    CheckForFreq(chunk[i]);
                if (!hasDate)
                    CheckForDate(chunk[i]);
                if (!hasTime)
                    CheckForTime(chunk[i]);
                 
                // Goto next chunk
                i++;
            }
                // If there is no SDF set it to manual
                if(!hasSDF) {
                    this.setSDF("MANUAL");
                }
                
                // Set SDFSOI variable
                this.setSDFSOI(this.getSDF() + "_" + this.getAnalyzedSOI());
                    
                // Check if it has all the peices
                if(FinalCheck()) {
                    parsed=true;
                    System.out.println("Processed signal successfully!");
                } else {
                    hasError = true;
                }            
        }
        else {
            hasError = true;
        }
    }
    
    public void CheckForSDF(String input, String input2) {
        for(int x=0; x<SDFtypes.length; x++) {
            if(input.equals(SDFtypes[x])) {
                this.setSDF(input + "_" + input2);
                hasSDF = true;
                System.out.println(this.getSDF());
                System.out.println("Found the SDF!");
                i++;
                break;
            }       
        }
        if(!hasSDF) {
            //Still didn't find an SDF      
        }
    }
    
    public void CheckForFreq(String input) {
        for(int i=0; i<freqTypes.length; i++) {
            // Check if it contains a decimal
            if(input.contains(".")) {
                // Check if string contains a freq abbreviation
                if(input.toLowerCase().contains(freqTypes[i].toLowerCase())) {
                    input = input.toLowerCase().replace(freqTypes[i].toLowerCase(), "");
                    this.setFreq(input);
                    System.out.println("Frequency: " + input);
                    hasFreq = true;
                    System.out.println("Found the Frequency!");
                }
            }
        }
    }
    
    public void CheckForDate(String input) {
        // Check if the input has 6 characters YYMMDD
        if(input.length() == 6 && isNumeric(input)) {
            this.setDate(input);
            hasDate = true;
            System.out.println(input);
            System.out.println("Found the Date!");
        }
    }
    
    public void CheckForTime(String input) {
            try {
                if(input.toLowerCase().substring(input.length()-1,input.length()).equals("z")) {
                    //Try removing the Z and check if its numeric
                    if(isNumeric(input.toLowerCase().replace("z",""))) {
                        // It's numeric and probably the time
                        hasTime = true;
                        System.out.println(input);
                        System.out.println("Found the Time!");
                        this.setTime(input);
                    }
                }
            }
            catch(StringIndexOutOfBoundsException e) {
                // Do nothing
            }       
    }
    
    public void setSDF(String s) {
        this.SDF = s;
    }
    
    public void setSDFSOI(String s) {
        this.SDFSOI = s;
    }
    
    public void setFreq(String f) {
        this.freq = f;
    }
    
    public void setDate(String s) {
        this.date = s;
    }
    
    public String getMission() {
        return this.mission;
    }

    public String getSDFSOI() {
        return this.SDFSOI;
    }
    
    public String getName() {
        return this.filename;
    }
    
    public String getSDF() {
        return this.SDF;
    }

    public void setAnalyzedSOI(String s) {
        this.analyzedSOI = s;
        wasAnalyzed = true;
    }
    
    public boolean getTime() {
        return this.hasTime;
    }
    
    public String getAnalyzedSOI() {
        return this.analyzedSOI;
    }
    
    public String getSOI() {
        return this.SOI;
    }
    
    public String getFilename() {
        return this.filename;
    }
    
    public void setTime(String t) {
        this.time = t;
    }
    
    boolean FinalCheck() {
        if(hasFreq == true && hasDate == true && hasTime == true && hasSOI == true)
            return true;
        else
            return false;
    }
    
    public static boolean isNumeric(String str) {  
        try  {  
            double d = Double.parseDouble(str);  
        }  
        catch(NumberFormatException nfe) {  
            return false;  
        }  
            return true;  
    }   
}
