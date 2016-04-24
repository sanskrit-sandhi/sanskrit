package cse.iitd;


public class IAST1ToSLP
{

    public IAST1ToSLP(){}

public static String transform(String transformed){
    transformed = transformed.toLowerCase();
    //System.out.println("IASTToSLP: " + transformed  );
    //Ä�
    // Vowels
    transformed = transformed.replaceAll( "a1","A" ); 
    transformed = transformed.replaceAll("i1" ,"I"); 
    transformed = transformed.replaceAll( "u1", "U");
    transformed = transformed.replaceAll("r2" ,"f"); 
    transformed = transformed.replaceAll( "r21" , "F"); 
    transformed = transformed.replaceAll( "l2", "x"); 
    transformed = transformed.replaceAll( "l21", "X"); 
   
    transformed = transformed.replaceAll("ai","E");
    transformed = transformed.replaceAll("au","O");
    
    transformed = transformed.replaceAll( "h2", "H"); 
    transformed = transformed.replaceAll( "m2","M");
    
    transformed = transformed.replaceAll("kh","K");
    transformed = transformed.replaceAll("gh","G");

    transformed = transformed.replaceAll("ch","C");
    transformed = transformed.replaceAll("jh","J");


    transformed = transformed.replaceAll( "t2h", "W");
    transformed = transformed.replaceAll( "t2", "w");  
    
    transformed = transformed.replaceAll( "d2h" , "Q");
    // vargiyas
    transformed = transformed.replaceAll( "d2" , "q"); 

    transformed = transformed.replaceAll("th","T"); 
    transformed = transformed.replaceAll("dh","D"); 

    transformed = transformed.replaceAll( "ph", "P"); 
    transformed = transformed.replaceAll( "bh", "B"); 

    // Nasals:
    transformed = transformed.replaceAll( "n5","Y"); // represents
    // SLP
    // "Y"(jYaana)
    transformed = transformed.replaceAll( "n3","N"); // represents
    // SLP
    // "N"(kalaNka)
    transformed = transformed.replaceAll( "n2","R"); // represents
    // SLP
    // "R"(N)
    transformed = transformed.replaceAll("s4", "S"); // represents
    // SLP
    // "S"(Sh
    // as
    // in
    // Sharma)

    transformed = transformed.replaceAll("s2","z"); // represents
    // SLP
    // "z"(kzaNa)
    return transformed;
    }
}

