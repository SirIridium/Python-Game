public class Sign{
    public static void main(String[] args) {
        
    String tester = "aaabbbcccdddeeefffggghh";
    int width = 3; 
    int start = 0; int end = width; String result = ""; 
    while(tester.substring(start).length() > 3){
        result += tester.substring(start,end) + ";";
        System.out.println(tester.substring(start,end));
        start = end;
        end += width;
    }
    result+=(tester.substring(start)); 
    System.out.println(result); 
    System.out.println((5/2)+1);
    }
}