i=0
j=0
numErrors = 0
filename = "BMSData2.txt"
line = ""
c = ''
op1 = "DFHMDI"
op2 = "DFHMDF"
op3 = "DFHMSD"
emptyOp = "      "
end = "END"
empty = "               "


print("What file do you want to load?\n")
#filename = raw_input()
output = open("BMSOut.txt", "w")

def CheckColOne(line):
    global numErrors
    if (not((line[0]==' ')or(line[0]=='*')or(line[0].isalpha() and line[0].isupper()))):
        output.write("ERROR (first character)\n")
        print("ERROR (first character)\n")
        numErrors = numErrors +1
    
def LabelTooLong(line):
    global numErrors
    if(line[0].isalpha() and line[0].isupper()):
    
        if line[7].isalpha() or line[7].isdigit():
        
            print("ERROR (Label Too Long)\n")
            output.write("ERROR (Label Too Long)\n")
            numErrors = numErrors + 1
            
def NonBlank(line):
    global numErrors
    if(len(line)< 8):
        return
    if(not((line[7]==' ')and(line[8]==' '))):
    
         if(not(line[0]=='*')):
            print("ERROR (Non-Blank in 8 or 9)\n")
            output.write("ERROR (Non-Blank in 8 or 9)\n")
            numErrors = numErrors + 1
        

    
def IllegalOpCode(line):
    global numErrors
    if(len(line)< 15):
        return
    if(line[0]==' ' or (line[0].isalpha() and line[0].isupper())):
        if((line[9].isalpha() and line[9].isupper()) and (line[15]==' ')):
            print line.find(op1)
           # if ("DFHMDI" not in line) or ("DFHMDF" not in line) or ("DFHMSD" not in line) or ("      " not in line) or ("               " not in line):
            if not((line.find(op1)==9) or (line.find(op2)==9) or (line.find(op3)==9) or (line.find(emptyOp)==9) or (line.find(end)==9)): 
                print("ERROR (Illegal Op Code)\n")
                output.write("ERROR (Illegal Op Code)\n")
                numErrors = numErrors + 1

def OpcodeWrongCol(line):
    global numErrors
    print "OpCodeWrongCol"
def OperandWrongCol(line):
    global numErrors
    print "OperandWrongCol"
def EndingInEnd(line):
    global numErrors
    print "EndingInEnd"

def main(filename):
  f = open(filename,"r")
  
  line = f.readline() #first line
  while line:
    output.write(line)    
    print line
    
    CheckColOne(line)
    LabelTooLong(line)
    NonBlank(line)
    IllegalOpCode(line)
    OpcodeWrongCol(line)
    OperandWrongCol(line)
    
    line = f.readline() #reads next line
  EndingInEnd(line)
  output.write('\nEnd of Processing - ')
  output.write(str(numErrors))
  output.write(' errors encountered')

    
main(filename) #function call