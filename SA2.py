class SyntaxAnalyzer:
    def __init__(self,tokens):
        self.ts = tokens
        self.index = 0
        
    def parser(self):
        if self.start(): #12
            print('No Syntax Error')
        else:
            print(f'Syntax error at {self.ts[self.index][2]}')
        
    def start(self):
        if self.ts[self.index][0] in ['Access Modifier','Class','Abstract', 'Interface']:
            if self.withAMBody(): #21
                if self.start(): #12
                    return True
                elif self.ts[self.index][0] == "$":
                    return True
        # print('Error start() => ',self.ts[self.index])
        return False
    
    def withAMBody(self):
        if self.AM_St(): #29
            if self.NBody(): #40
                return True
        # print('Error withAMBody() => ',self.ts[self.index])
        return False
    
    def AM_St(self):
        if self.ts[self.index][0] == 'Access Modifier':
            print('Match AM_St() => ',self.ts[self.index])
            self.index += 1
            return True
        elif self.ts[self.index][0] in ['Constant','Static', 'Virtual', 'Override', 'Void','[', 'Identifier','Class','Abstract', 'Interface']:
            return True
        else:
            # print('Error AM_St() => ',self.ts[self.index])
            return False
        
    def NBody(self):
        if self.classSt(): #49
            return True
        elif self.interfaceSt(): #70
            return True
        else:
            # print('Error NBody() => ',self.ts[self.index])
            return False

        
    def classSt(self):
        if self.abstractSt(): #89
            if self.ts[self.index][0] == 'Class':
                print('Match classSt()-1 => ',self.ts[self.index])
                self.index += 1
                if self.ts[self.index][0] == 'Identifier':
                    print('Match classSt()-2 => ',self.ts[self.index])
                    self.index += 1
                    if self.inheritSt(): #100
                        if self.ts[self.index][0] == '{':
                            print('Match classSt()-3 => ',self.ts[self.index])
                            self.index += 1
                            if self.classList(): #117
                                if self.ts[self.index][0] == '}':
                                    print('Match classSt()-4 => ',self.ts[self.index])
                                    self.index += 1
                                    return True
        # print('Error classSt() => ',self.ts[self.index])
        return False
        
    def interfaceSt(self):
        if self.ts[self.index][0] == 'Interface':
            print('Match interfaceSt()-1 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == 'Identifier':
                print('Match interfaceSt()-2 => ',self.ts[self.index])
                self.index += 1
                if self.ts[self.index][0] == '{': 
                    print('Match interfaceSt()-3 => ',self.ts[self.index])
                    self.index += 1
                    if self.interfaceMethod2(): #129
                         if self.ts[self.index][0] == '}':
                                print('Match interfaceSt()-4 => ',self.ts[self.index])
                                self.index += 1
                                return True
        # print('Error interfaceSt() => ',self.ts[self.index])
        return False
        
    def abstractSt(self):
        if self.ts[self.index][0] == 'Abstract':
            print('Match abstractSt() => ',self.ts[self.index])
            self.index += 1
            return True
        elif self.ts[self.index][0] == 'Class':
            return True
        # print('Error abstractSt() => ',self.ts[self.index])
        return False
        
    def inheritSt(self):
        if self.ts[self.index][0] == ':':
            print('Match inheritSt()-1 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == 'Identifier':
                print('Match inheritSt()-2 => ',self.ts[self.index])
                self.index += 1
                return True
            else:
                print('Error inheritSt()-1 => ',self.ts[self.index])
                return False
        elif self.ts[self.index][0] == '{':
            return True
        print('Error inheritSt()-2 => ',self.ts[self.index])
        return False
        
    def classList(self):
        if self.ts[self.index][0] in ['Constant', 'Access Modifier','Static', 'Virtual', 'Override', 'Data Type' 'Void', 'Identifier','Class','Abstract', 'Interface']:
            if self.withAM(): #145
                if self.classList():
                    return True
        else:
            if self.ts[self.index][0] == '}':
                return True
        print('Error classList() => ',self.ts[self.index])
        return False
            
    def interfaceMethod2(self):
        if self.interfaceMethod():
            if self.ts[self.index][0] == ';': 
                    print('Match interfaceMethod2() => ',self.ts[self.index])
                    self.index += 1
                    if self.interfaceMethod2(): #153
                        return True
            else:
                print('Error interfaceMethod2()-1 => ',self.ts[self.index])
                return False
        elif self.ts[self.index][0] == '}':
            return True
        print('Error interfaceMethod2()-2 => ',self.ts[self.index])
        return False
        
    def withAM(self):
        if self.AM_St(): #29
            if self.staticOrVoid(): #173
                return True
        print('Error interfaceMethod2()-2 => ',self.ts[self.index])
        return False
    
    def interfaceMethod(self): #doubt 2538
        if self.ts[self.index][0] == 'Void' or self.DataTypesForConst(): #189
            if self.ts[self.index][0] == 'Void':
                self.index += 1
                print('Match interfaceMethod()-1 => ',self.ts[self.index])
            if self.ts[self.index][0] == 'Identifier':
                print('Match interfaceMethod()-2 => ',self.ts[self.index])
                self.index += 1           
                if self.ts[self.index][0] == '(':
                    print('Match interfaceMethod()-3 => ',self.ts[self.index])
                    self.index +=1
                    if self.args(): #205
                        if self.ts[self.index][0] == ')':
                            print('Match interfaceMethod()-4 => ',self.ts[self.index])
                            self.index +=1
                            return True
        print('Error interfaceMethod() => ',self.ts[self.index])
        return False
        
    def staticOrVoid(self):
        if self.ts[self.index][0] == 'Static':
            print('Match staticOrVoid() => ',self.ts[self.index])
            self.index += 1
            if self.AMList(): #215
                return True
        elif self.ts[self.index][0] == 'Virtual/Override':
            if self.override(): #224
                return True
        elif self.ts[self.index][0] in ['Data Type', 'Void', 'Identifier','Constant']:
            if self.AMList(): #215
                return True
        print('Error staticOrVoid() => ',self.ts[self.index])
        return False
           
    def DataTypesForConst(self):
        if self.ts[self.index][0] == 'Data Type':
            print('Match DataTypesForConst()-1 => ',self.ts[self.index])
            self.index += 1
            if self.DataType2List(): #234
                return True
            if self.ts[self.index][0] == 'Identifier':
                print('Match DataTypesForConst()-2 => ',self.ts[self.index])
                self.index += 1
                if self.DataType2List():#234
                    return True
        print('Error DataTypesForConst() => ',self.ts[self.index])
        return False
        
    def args(self):
        if self.ts[self.index][0] == 'Data Type' or self.ts[self.index][0] == 'Identifier':
            if self.argsList(): #250
                return True
        elif self.ts[self.index][0] == ')':
            return True
        print('Error args() => ',self.ts[self.index])
        return False
    
    def AMList(self):
        if self.AMList2(): #264
            return True
        elif self.NBody(): #40
            return True
        else:
            print('Error AMList() => ',self.ts[self.index])
            return False
        
    def override(self):
        if self.ts[self.index][0] == 'Virtual/Override':
            print('Match override() => ',self.ts[self.index])
            self.index += 1
            if self.overrideList(): #282
                return True
        print('Error override() => ',self.ts[self.index])
        return False
        
    def DataType2List(self): #2D-array
        if self.ts[self.index][0] == '[':
            print('Match DataType2List()-1 => ',self.ts[self.index])
            self.index += 1
            return True
        elif self.ts[self.index][0] == ',':
            print('Match DataType2List()-2 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == ']':
                print('Match DataType2List()-3 => ',self.ts[self.index])
                self.index += 1
                return True
        print('Error DataType2List() => ',self.ts[self.index])
        return False
        
    def argsList(self):
        if self.argsDataType(): #294
            if self.argsSt(): #304
                return True
        elif self.ts[self.index][0] == 'Identifier':
            print('Match argsList() => ',self.ts[self.index])
            self.index += 1
            if self.ID3St(): #316
                if self.argsSt(): #304
                    return True
        print('Error argsList() => ',self.ts[self.index])
        return False
        
    def AMList2(self):
        if self.constSt(): #325
            return True
        elif self.DT_Types(): #341
            if self.MF():
                return True
        elif self.ts[self.index][0] == 'Void':
            print('Match AMList2()-1 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == 'Identifier':
                print('Match AMList2()-2 => ',self.ts[self.index])
                self.index += 1
                if self.method(): #362
                    return True
        print('Error AMList2() => ',self.ts[self.index])
        return True
        
    def overrideList(self):
        if self.ts[self.index][0] == 'Data Type' or self.ts[self.index][0] == 'Void':
            if self.DT_Types(): #341
                if self.ts[self.index][0] == 'Identifier':
                    print('Match overrideList() => ',self.ts[self.index])
                    self.index += 1
                    if self.method(): #362
                        return True
        print('Error overrideList() => ',self.ts[self.index])
        return False
            
    def argsDataType(self):
        if self.ts[self.index][0] == 'Data Type':
            print('Match argsDataType() => ',self.ts[self.index])
            self.index += 1
            if self.argsDTList(): #379
                return True
        print('Error argsDataType() => ',self.ts[self.index])
        return False
    
    def argsSt(self):
        if self.ts[self.index][0] == ',':
            print('Match argsSt() => ',self.ts[self.index])
            self.index += 1
            if self.args(): #205
                return True
        elif self.ts[self.index][0] == ')':
            return True
        print('Error argsSt() => ',self.ts[self.index])
        return False
    
    def ID3St(self):
        if self.argsObj(): #391
            return True
        elif self.argsArr5(): #405
            return True
        else:
            print('Error ID3St() => ',self.ts[self.index])
            return False
    
    def constSt(self):
        if self.ts[self.index][0] == 'Constant':
            print('Match constSt()-1 => ',self.ts[self.index])
            self.index += 1
            if self.DataTypesForConst(): #190
                if self.ts[self.index][0] == 'Identifier':
                    print('Match constSt()-2 => ',self.ts[self.index])
                    self.index += 1
                    if self.allInit(): #411
                        if self.ts[self.index][0] == ';':
                            print('Match constSt()-3 => ',self.ts[self.index])
                            self.index += 1
        print('Error constSt() => ',self.ts[self.index])
        return False
    
    def DT_Types(self):
        if self.ts[self.index][0] == 'Data Type':
            print('Match DT_Types()-1 => ',self.ts[self.index])
            self.index += 1
            if self.DT2List(): #423
                return True
        if self.ts[self.index][0] == 'Identifier':
            print('Match DT_Types()-2 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == '(':
                if self.construct(): #436
                    return True
            elif self.ts[self.index][0] == '[':
                if self.DT2List(): #234
                    return True
            elif self.ts[self.index][0] == 'Identifier':
                return True
        print('Error DT_Types() => ',self.ts[self.index])
        return False
        
    def method(self):
        if self.ts[self.index][0] == '(':
            print('Match method()-1 => ',self.ts[self.index])
            self.index += 1
            if self.args(): #205
                if self.ts[self.index][0] == ')':
                    print('Match method()-2 => ',self.ts[self.index])
                    self.index += 1
                    if self.ts[self.index][0] == '{':
                        print('Match method()-3 => ',self.ts[self.index])
                        self.index += 1
                        if self.MST(): #456
                            if self.ts[self.index][0] == '}':
                                print('Match method()-4 => ',self.ts[self.index])
                                self.index += 1
                                return True

        print('Error method() => ',self.ts[self.index])
        return False
        
    def argsDTList(self):
        if self.ts[self.index][0] == 'Identifier':
            print('Match argsDTList() => ',self.ts[self.index])
            self.index += 1
            if self.argsInit(): #438
                return True
        elif self.argsArr5(): #405
            return True
        print('Error argsDTList() => ',self.ts[self.index])
        return False
    
    def argsObj(self):
        if self.ts[self.index][0] == 'Identifier':
            print('Match argsObj() => ',self.ts[self.index])
            self.index += 1
            if self.argsInit(): #438
                return True
        print('Error argsObj() => ',self.ts[self.index])
        return False
        
    def argsArr5(self):
        if self.ts[self.index][0] == '[':
            print('Match argsArr5() => ',self.ts[self.index])
            self.index += 1
            if self.argsArr5List(): #488
                return True
        print('Error argsArr5() => ',self.ts[self.index])
        return False
        
    def allInit(self): #checked
        if self.ts[self.index][0] == 'Assignment Operator':
            if self.assign(): #512
                return True
            #i--
        else:
            if self.ts[self.index][0] == [';',',',')']:
                return True
        print('Error allInit() => ',self.ts[self.index])
        return False
            
    def DT2List(self):
        if self.ts[self.index][0] == '[':
            print('Match DT2List() => ',self.ts[self.index])
            self.index += 1 
            if self.DT2list2(): #522
                return True
        else:
            if self.ts[self.index][0] == 'Identifier':
                return True
        print('Error DT2List() => ',self.ts[self.index])
        return False
    
    def construct(self):
        if self.ts[self.index][0] == '(':
            print('Match construct()-1 => ',self.ts[self.index])
            self.index += 1
            if self.args(): #205
                if self.ts[self.index][0] == ')':
                    print('Match construct()-2 => ',self.ts[self.index])
                    self.index += 1
                    if self.superClass(): #506
                        if self.ts[self.index][0] == '{':
                            print('Match construct()-3 => ',self.ts[self.index])
                            self.index += 1
                            if self.MST(): #456
                                if self.ts[self.index][0] == '}':
                                    print('Match construct()-4 => ',self.ts[self.index])
                                    self.index += 1
        print('Error construct() => ',self.ts[self.index])
        return False
        
    def MST(self):
        if self.ts[self.index][0] in ['Constant','Static','Identifier','Data Type', 'For', 'Continue', 'Break', 'Return', 'If', 'This']:
            if self.SST(): #526
                if self.MST(): #456
                    return True
        elif self.ts[self.index][0] == '}':
            return True
        print('Error MST() => ',self.ts[self.index])
        return False
        
    def argsInit(self):
        if self.ts[self.index][0] == 'Assignment Operator':
            print('Match argsInit()-1 => ',self.ts[self.index])
            self.index += 1
            if self.OE2(): #575
                return True
        elif self.ts[self.index][0] == 'New':
            print('Match argsInit()-2 => ',self.ts[self.index])
            self.index += 1
            if self.assignList(): #589
                return True
        elif self.ts[self.index][0] == '{':
            if self.BInit(): #598
                return True
        else:
            if self.ts[self.index][0] == ')' or self.ts[self.index][0] == ',':
                return True
            else:
                print('Error argsInit() => ',self.ts[self.index])
                return False
            
    def argsArr5List(self):
        if self.ts[self.index][0] == ']':
            print('Match argsArr5List()-1 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == 'Identifier':
                print('Match argsArr5List()-2 => ',self.ts[self.index])
                self.index += 1
                if self.argsInit(): #467
                    return True
        elif self.ts[self.index][0] == ',':
            print('Match argsArr5List()-3 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == ']':
                print('Match argsArr5List()-4 => ',self.ts[self.index])
                self.index += 1
                if self.ts[self.index][0] == 'Identifier':
                    print('Match argsArr5List()-5 => ',self.ts[self.index])
                    self.index += 1
                    if self.argsInit(): #467
                        return True
        print('Error argsArr5List() => ',self.ts[self.index])
        return False
        
    def assign(self): #checked
        if self.ts[self.index][0] == 'Assignment Operator':
            print('Match assign() => ',self.ts[self.index])
            self.index += 1
            if self.values(): #607
                return True
        print('Error assign() => ',self.ts[self.index])
        return False
        
    def DT2list2(self): #2D-array
        if self.ts[self.index][0] == ']':
            print('Match DT2list2()-1 => ',self.ts[self.index])
            self.index += 1
            return True
        elif self.ts[self.index][0] == ',':
            print('Match DT2list2()-2 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == ']':
                print('Match DT2list2()-3 => ',self.ts[self.index])
                self.index += 1
                return True
        print('Error DT2list2() => ',self.ts[self.index])
        return False
        
    def superClass(self):
        if self.ts[self.index][0] == ':':
            print('Match superClass()-1 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == 'Base':
                print('Match superClass()-2 => ',self.ts[self.index])
                self.index += 1
                if self.ts[self.index][0] == '(':
                    print('Match superClass()-3 => ',self.ts[self.index])
                    self.index += 1
                    if self.params(): #626
                        if self.ts[self.index][0] == ')':
                            print('Match superClass()-4 => ',self.ts[self.index])
                            self.index += 1
            print('Error superClass()-1 => ',self.ts[self.index])
            return False
        elif self.ts[self.index][0] == '{':
            return True
        print('Error superClass()-2 => ',self.ts[self.index])
        return False
    
    def SST(self):
        if self.withId(): #636
            if self.ts[self.index][0] == ';':
                print('Match SST()-1 => ',self.ts[self.index])
                self.index += 1
                return True
        elif self.withStaticConstDT(): #643
            if self.ts[self.index][0] == ';':
                print('Match SST()-2 => ',self.ts[self.index])
                self.index += 1
                return True
        elif self.forSt(): #651
            return True
        elif self.ifElse(): #675
            return True
        elif self.ts[self.index][0] == 'Continue':
            print('Match SST()-3 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == ';':
                print('Match SST()-4 => ',self.ts[self.index])
                self.index += 1
                return True
        elif self.ts[self.index][0] == 'Break':
            print('Match SST()-5 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == ';':
                print('Match SST()-6 => ',self.ts[self.index])
                self.index += 1
                return True
        elif self.ts[self.index][0] == 'Return':
            print('Match SST()-7 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == ';':
                print('Match SST()-8 => ',self.ts[self.index])
                self.index += 1
                return True
        elif self.ts[self.index][0] == 'This':
            print('Match SST()-9 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == '.':
                print('Match SST()-10 => ',self.ts[self.index])
                self.index += 1
                if self.withId(): #636
                    if self.ts[self.index][0] == ';':
                        print('Match SST()-11 => ',self.ts[self.index])
                        self.index += 1
                        return True
        print('Error SST() => ',self.ts[self.index])
        return False
    
    def OE2(self):
        if self.FWID(): #692
            if self.alles(): #718
                return True
        elif self.ts[self.index][0] == 'Identifier':
            print('Match OE2() => ',self.ts[self.index])
            self.index += 1
            if self.assign3(): #747
                return True
        print('Error OE2() => ',self.ts[self.index])
        return False
    
    def assignList(self):
        if self.ts[self.index][0] == 'Identifier' or self.ts[self.index][0] == 'Data Type':
            print('Match assignList() => ',self.ts[self.index])
            self.index += 1
            if self.assignList2(): #765
                return True
        print('Error assignList() => ',self.ts[self.index])
        return False
    
    def BInit(self):
        if self.ts[self.index][0] == '{':
            print('Match BInit() => ',self.ts[self.index])
            self.index += 1
            if self.BInitList(): #783
                return True
        print('Error BInit() => ',self.ts[self.index])
        return False
    
    def values(self): #checked
        if self.ts[self.index][0] in ['Identifier','Integer Constant','Float Constant','Char Constant','String Constant', 'NOT', '(', 'Increment/Decrement Opeartor']: #Not !
            if self.init(): #798
                return True
        elif self.ts[self.index][0] == 'New':
            print('Match values()-1 => ',self.ts[self.index])
            self.index += 1
            if self.assignList(): #589
                return True
        elif self.ts[self.index][0] == '{':
            if self.BInit(): #598
                return True
        elif self.ts[self.index][0] == 'Identifier':
            print('Match values()-2 => ',self.ts[self.index])
            if self.init2(): #805
                return True
        print('Error values() => ',self.ts[self.index])
        return False
    
    def params(self):
        if self.ts[self.index][0] in ['{','Identifier','New','Integer Constant','Float Constant','Char Constant','String Constant', 'Logical Operator','(', 'Increment/Decrement Opeartor']: #Not !
            if self.param2(): #823
                return True
        else:
            if self.ts[self.index][0] == ')':
                return True
        print('Error params() => ',self.ts[self.index])
        return False
    
    def withId(self): #checked
        if self.ts[self.index][0] == 'Identifier':
            print('Match withId() => ',self.ts[self.index])
            self.index += 1
            if self.list_(): #836
                return True
        print('Error withId() => ',self.ts[self.index])
        return False
    
    def withStaticConstDT(self):
        if self.staticSt(): #858
            if self.constSt2(): #868
                if self.withDT(): #879
                    return True
        print('Error withStaticConstDT() => ',self.ts[self.index])
        return False
            
    def forSt(self):
        if self.ts[self.index][0] == 'For':
            print('Match forSt()-1 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == '(':
                print('Match forSt()-2 => ',self.ts[self.index])
                self.index += 1
                if self.C1(): #888
                    if self.ts[self.index][0] == ';':
                        print('Match forSt()-3 => ',self.ts[self.index])
                        self.index += 1
                        if self.C2(): #898
                            if self.ts[self.index][0] == ';':
                                print('Match forSt()-4 => ',self.ts[self.index])
                                self.index += 1
                                if self.C3(): #906
                                    if self.ts[self.index][0] == ')':
                                        print('Match forSt()-5 => ',self.ts[self.index])
                                        self.index += 1
                                        if self.checkTerminator() or self.body(): #914 #922
                                            return True
        print('Error forSt() => ',self.ts[self.index])
        return False
    
    def ifElse(self):
        if self.ts[self.index][0] == 'If':
            print('Match ifElse()-1 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == '(':
                print('Match ifElse()-2 => ',self.ts[self.index])
                self.index += 1
                if self.OE(): #936
                    if self.ts[self.index][0] == ')':
                        print('Match ifElse()-3 => ',self.ts[self.index])
                        self.index += 1
                        if self.body(): #922
                            if self.ifList(): #943
                                return True
        print('Error ifElse() => ',self.ts[self.index])
        return False
    
    def FWID(self):
        if self.const(): #956
            return True
        elif self.ts[self.index][0] == 'NOT':
            print('Match FWID()-1 => ',self.ts[self.index])
            self.index += 1
            if self.F(): #976
                return True
        elif self.ts[self.index][0] == '(':
            print('Match FWID()-2 => ',self.ts[self.index])
            self.index += 1
            if self.OE2(): #577
                if self.alles(): #718
                    if self.ts[self.index][0] == ')':
                        print('Match FWID()-3 => ',self.ts[self.index])
                        self.index += 1
                        return True
        elif self.ts[self.index][0] == 'Increment/Decrement Opeartor':
            print('Match FWID()-4 => ',self.ts[self.index])
            self.index += 1
            if self.IDSt2(): #1016
                if self.alles(): #718
                    return True
        print('Error FWID() => ',self.ts[self.index])
        return False
    
    def alles(self):
        if self.OE_(): #1036
            if self.ts[self.index][0] in ['Arithmetaic Operator', 'Logical Operator', 'Relational Operator']:
                if self.alles(): #718
                    return True
            return True
        elif self.AE_(): #1050  smae for OR AND
            if self.ts[self.index][0] in ['Arithmetaic Operator', 'Logical Operator', 'Relational Operator']:
                if self.alles(): #718
                    return True
            return True
        elif self.RE_(): #1064
            if self.ts[self.index][0] in ['Arithmetaic Operator', 'Logical Operator', 'Relational Operator']:
                if self.alles(): #718
                    return True
                return True
        elif self.E_():
            if self.ts[self.index][0] in ['Arithmetaic Operator', 'Logical Operator', 'Relational Operator']:
                if self.alles(): #718
                    return True
                return True
        elif self.T_():
            if self.ts[self.index][0] in ['Arithmetaic Operator', 'Logical Operator', 'Relational Operator']:
                if self.alles(): #718
                    return True
            return True
        print('Error alles() => ',self.ts[self.index])
        return False
    
    def assign3(self):
         if self.ts[self.index][0] in ['.','[', '(', 'Increment/Decrement Opeartor', 'Arithmetaic Operator', 'Relational Operator', 'Assignment Operator']:
                if self.ts[self.index][0] == 'Assignment Operator':
                    if self.assign(): #482
                        return True
                elif self.ts[self.index][0] in ['Arithmetaic Operator', 'Logical Operator', 'Relational Operator']:
                    if self.alles(): #718
                        return True
                elif self.ts[self.index][0] in ['.', '[', '(','Increment/Decrement Opeartor']:
                    if self.OEList(): #1078
                        if self.alles(): #718
                            return True
                else:
                    if self.ts[self.index][0] == ';' or self.ts[self.index][0] == ',':
                        return True
                print('Error assign3() => ',self.ts[self.index])
                return False




    # def assign3(self):
    #     if self.ts[self.index][0] in ['.','[', '(', 'Increment/Decrement Opeartor', 'Arithmetaic Operator', 'Relational Operator', 'Assignment Operator']:
    #         if self.ts[self.index][0] == 'Assignment Operator':
    #             if self.assign(): #482
    #                 return True
    #         elif self.ts[self.index][0] in ['Arithmetaic Operator', 'Logical Operator', 'Relational Operator']:
    #             if self.alles(): #718
    #                 return True
    #         elif self.ts[self.index][0] in ['.', '[', '(','Increment/Decrement Opeartor']:
    #             if self.OEList(): #1078
    #                 if self.alles(): #718
    #                     return True
    #     else:
    #         if self.ts[self.index][0] == ';' or self.ts[self.index][0] == ',':
    #             return True
    #     print('Error assign3() => ',self.ts[self.index])
    #     return False



    def assignList2(self):
        if self.ts[self.index][0] == '[':
            print('Match assignList2()-1 => ',self.ts[self.index])
            self.index += 1
            if self.OE(): #936
                if self.assignList3(): #1098
                    return True
        elif self.ts[self.index][0] == '(': 
            print('Match assignList2()-2 => ',self.ts[self.index])
            self.index += 1
            if self.params(): #626
                if self.ts[self.index][0] == ')':
                    print('Match assignList2()-3 => ',self.ts[self.index])
                    self.index += 1
                    return True
            print('Error assignList2() => ',self.ts[self.index])
            return False
        
    def BInitList(self):
        if self.ts[self.index][0] in ['Identifier','Integer Constant','Float Constant','Char Constant','String Constant', 'NOT', '(', 'Increment/Decrement Opeartor']:
            if self.arrConst0(): #1114
                if self.ts[self.index][0] == '{':
                    print('Match BInitList()-1 => ',self.ts[self.index])
                    self.index += 1
                    return True
        elif self.arrConst2(): #1124
            if self.ts[self.index][0] == '}':
                print('Match BInitList()-2 => ',self.ts[self.index])
                self.index += 1
                return True
        print('Error BInitList() => ',self.ts[self.index])
        return False
    
    def init(self):
        if self.OE2(): #577
            if self.init3(): #1134
                return True
        print('Error init() => ',self.ts[self.index])
        return False
    
    def init2(self):
        if self.assign(): #482
            return True
        elif self.functionCall(): #1150
            return True
        elif self.objectCall(): #1162
            return True
        elif self.arr4(): #1174
            return True
        elif self.init3(): #1134
            return True
        elif self.incDec(): #1181
            return True
        elif self.ts[self.index][0] == ';':
            return True
        print('Error init2() => ',self.ts[self.index])
        return False
    
    def param2(self):
        if self.OE(): #936
            if self.param3(): #1189
                return True
        elif self.ts[self.index][0] == 'New':
            print('Match param2() => ',self.ts[self.index])
            self.index += 1
            if self.assignList(): #589
                if self.param3(): #1189
                    return True
        print('Error param2() => ',self.ts[self.index])
        return False
    
    def list_(self): #checked
        if self.ts[self.index][0] == 'Assignment Operator':
            if self.assign(): #482
                return True
        elif self.ts[self.index][0] == '(':
            if self.functionCall(): #1150
                return True
        elif self.ts[self.index][0] == '[':
            if self.arr(): #1020
                return True
        elif self.ts[self.index][0] == 'Identifier':
            if self.obj(): #1211
                return True
        elif self.ts[self.index][0] == '.':
            if self.objectCall(): #1162
                return True
        elif self.ts[self.index][0] == 'Increment/Decrement Opeartor':
            if self.incDec(): #1181
                return True
        print('Error list_() => ',self.ts[self.index])
        return False
    
    def staticSt(self):
        if self.ts[self.index][0] == 'Static':
            print('Match staticSt() => ',self.ts[self.index])
            self.index += 1
            return True
        elif self.ts[self.index][0] in ['Virtual/Override', 'Data Type', 'Void', 'Identifier', 'Constant']:
            return True
        print('Error staticSt() => ',self.ts[self.index])
        return False
    
    def constSt2(self):
        if self.ts[self.index][0] == 'Constant':
            print('Match constSt2() => ',self.ts[self.index])
            self.index += 1
            return True
        else:
            if self.ts[self.index][0] == 'Data Type' or self.ts[self.index][0] == 'Identifier':
                return True
        print('Error constSt2() => ',self.ts[self.index])
        return False
    
    def withDT(self):
        if self.ts[self.index][0] == 'Data Type':
            print('Match withDT() => ',self.ts[self.index])
            self.index += 1
            if self.DTList(): #1220
                return True
        print('Error withDT() => ',self.ts[self.index])
        return False
            
    def C1(self):
        if self.OE2(): #577
            return True
        elif self.withDT(): #879
            return True
        elif self.ts[self.index][0] == ';':
            return True
        print('Error C1() => ',self.ts[self.index])
        return False
    
    def C2(self):
        if self.OE(): #936
            return True
        elif self.ts[self.index][0] == ';':
            return True
        print('Error C2() => ',self.ts[self.index])
        return False
    
    def C3(self):
        if self.OE2(): #577
            return True
        elif self.ts[self.index][0] == ')':
            return True
        print('Error C3() => ',self.ts[self.index])
        return False
    
    def checkTerminator(self):
        if self.ts[self.index][0] == ';':
            print('Match checkTerminator() => ',self.ts[self.index])
            self.index += 1
            return True
        print('Error checkTerminator() => ',self.ts[self.index])
        return False
    
    def body(self):
        if self.SST(): #527
            return True
        elif self.ts[self.index][0] == '{':
            print('Match body()-1 => ',self.ts[self.index])
            self.index += 1
            if self.MST(): #428
                if self.ts[self.index][0] == '}':
                    print('Match body()-2 => ',self.ts[self.index])
                    self.index += 1
                    return True
        print('Error body() => ',self.ts[self.index])
        return False
    
    def OE(self): #checked
        if self.AE(): #1231
            if self.OE_(): #1036
                return True
        print('Error OE() => ',self.ts[self.index])
        return False
    
    def ifList(self):
        if self.ts[self.index][0] == 'Else':
            print('Match ifList() => ',self.ts[self.index])
            self.index += 1        
            if self.body(): #922
                return True
            print('Error ifList()-1 => ',self.ts[self.index])
            return False
        elif self.ts[self.index][0] in ['}','Constant','Static', 'Identifier', 'Data Type', 'For', 'Continue', 'Break', 'Return', 'If', 'This']:
            return True
        print('Error ifList()-2 => ',self.ts[self.index])
        return False
    
    def const(self):
        if self.ts[self.index][0] == 'Integer Constant':
            print('Match const()-1 => ',self.ts[self.index])
            self.index += 1
            return True
        if self.ts[self.index][0] == 'Float Constant':
            print('Match const()-2 => ',self.ts[self.index])
            self.index += 1
            return True
        if self.ts[self.index][0] == 'Char Constant':
            print('Match const()-3 => ',self.ts[self.index])
            self.index += 1
            return True
        if self.ts[self.index][0] == 'String Constant':
            print('Match const()-4 => ',self.ts[self.index])
            self.index += 1
            return True
        print('Error const() => ',self.ts[self.index])
        return False
            
    def F(self): #checked
        if self.ts[self.index][0] == 'Increment/Decrement Opeartor':
            print('Match F()-1 => ',self.ts[self.index])
            self.index += 1
            if self.incDecList(): #1238
                return True
        elif self.const(): #956
            return True
        elif self.ts[self.index][0] == '(':
            print('Match F()-2 => ',self.ts[self.index])
            self.index += 1
            if self.OE(): #936
                if self.ts[self.index][0] == ')':
                    print('Match F()-3 => ',self.ts[self.index])
                    self.index += 1
                    return True
        elif self.ts[self.index][0] == 'NOT':
                print('Match F()-3 => ',self.ts[self.index])
                self.index += 1
                if self.F(): #976
                    return True
        elif self.ts[self.index][0] == 'Identifier':
            print('Match F()-4 => ',self.ts[self.index])
            self.index += 1
            if self.OEList(): #1078
                return True
        elif self.ts[self.index][0] == 'This':
            print('Match F()-5 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == '.':
                print('Match F()-6 => ',self.ts[self.index])
                self.index += 1
                if self.ts[self.index][0] == 'Identifier':
                    print('Match F()-7 => ',self.ts[self.index])
                    self.index += 1
                    if self.OEList(): #1078
                        return True
        print('Error F() => ',self.ts[self.index])
        return False
    
    def IDSt2(self):
        if self.ts[self.index][0] == 'Identifier':
            print('Match F()-1 => ',self.ts[self.index])
            self.index += 1
            if self.chain(): #1258
                return True
        elif self.ts[self.index][0] == 'This':
            print('Match F()-2 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == '.':
                print('Match F()-3 => ',self.ts[self.index])
                self.index += 1
                if self.ts[self.index][0] == 'Identifier':
                    print('Match F()-4 => ',self.ts[self.index])
                    self.index += 1
                    if self.chain(): #1258
                        return True
        print('Error IDSt2() => ',self.ts[self.index])
        return False
    
    def OE_(self): #checked
        if self.ts[self.index][0] == 'Logical Operator': #OR
            print('Match OE_() => ',self.ts[self.index])
            self.index += 1
            if self.AE(): #1231
                if self.OE_(): #1036
                    return True
            print('Error OE_()-1 => ',self.ts[self.index])
            return False
        elif self.ts[self.index][0] in [';',',',')',']','}']:
            return True
        print('Error OE_()-1 => ',self.ts[self.index])
        return False
    
    def AE_(self): #checked
        if self.ts[self.index][0] == 'Logical Operator': #AND
            print('Match AE_() => ',self.ts[self.index])
            self.index += 1
            if self.RE(): #1275
                if self.AE_(): #1050
                    return True
            print('Error AE_()-1 => ',self.ts[self.index])
            return False
        elif self.ts[self.index][0] in [';',',',')',']','}']:
            return True
        print('Error AE_()-1 => ',self.ts[self.index])
        return False
                    
    def RE_(self): #checked
        if self.ts[self.index][0] == 'Relational Operator':
            print('Match RE_() => ',self.ts[self.index])
            self.index += 1
            if self.E(): #1282
                if self.RE_(): #1064
                    return True
            print('Error RE_()-1 => ',self.ts[self.index])
            return False
        elif self.ts[self.index][0] in ['Logical Operator',';',',',')',']','}']:
            return True
        print('Error RE_()-1 => ',self.ts[self.index])
        return False
    
    def OEList(self):
        if self.ts[self.index][0] in ['.','[','(','Increment/Decrement Opeartor']:
            if self.ts[self.index][0] == '(':
                if self.funcCallOE(): #1289
                    return True
            elif self.ts[self.index][0] == '.':
                if self.objCallOE(): #1300
                    return True
            elif self.ts[self.index][0] == '[':
                if self.ArrOE(): #1312
                    return True
            elif self.ts[self.index][0] == 'Increment/Decrement Opeartor':
                if self.incDec(): #1181
                    return True
        else:
            if self.ts[self.index][0] in ['Arithmetaic Operator','}','Relational Operator','Logical Operator',';',')',',','']:
                return True
        print('Error OEList() => ',self.ts[self.index])
        return False
    
    def assignList3(self):
        if self.ts[self.index][0] == ']':
            print('Match assignList3()-1 => ',self.ts[self.index])
            self.index += 1
            return True
        elif self.ts[self.index][0] == ',':
            print('Match assignList3()-2 => ',self.ts[self.index])
            self.index += 1
            if self.OE(): #936
                if self.ts[self.index][0] == ']':
                    print('Match assignList3()-1 => ',self.ts[self.index])
                    self.index += 1
        print('Error assignList3() => ',self.ts[self.index])
        return False
        
    def arrConst0(self):
        if self.ts[self.index][0] in ['Identifier','Integer Constant','Float Constant','Char Constant','String Constant', 'NOT', '(', 'Increment/Decrement Opeartor']:
            if self.arrConst(): #1322
                return True
            else:
                if self.ts[self.index][0] == '}':
                    return True
            print('Error arrConst0() => ',self.ts[self.index])
            return False
    
    def arrConst2(self):
        if self.ts[self.index][0] == '{':
            if self.arrConst3(): #1239
                return True
        else:
            if self.ts[self.index][0] == '}':
                return True
        print('Error arrConst2() => ',self.ts[self.index])
        return False
        
    def init3(self):
        if self.ts[self.index][0] == ',':
            print('Match init3()-1 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == 'Identifier':
                print('Match init3()-2 => ',self.ts[self.index])
                self.index += 1
                if self.assign(): #482
                    return True
                print('Error init3() => ',self.ts[self.index])
                return False
        elif self.ts[self.index][0] == ';':
            return True
        print('Error init3() => ',self.ts[self.index])
        return False
    
    def functionCall(self): #checked
        if self.ts[self.index][0] == '(':
            print('Match init3()-1 => ',self.ts[self.index])
            self.index += 1
            if self.params(): #626
                if self.ts[self.index][0] == ')':
                    print('Match init3()-2 => ',self.ts[self.index])
                    self.index += 1
                    if self.functionList(): #1164
                        return True
        print('Error functionCall() => ',self.ts[self.index])
        return False

    def functionList(self): #checked
        if self.ts[self.index][0] == '[' or self.ts[self.index][0] == '.':
            if self.ts[self.index][0] == '.':
                print('Match functionList()-1 => ',self.ts[self.index])
                self.index += 1
                if self.ts[self.index][0] == 'Identifier':
                    print('Match functionList()-2 => ',self.ts[self.index])
                    self.index += 1
                    if self.functionList2(): #
                        return True
            elif self.functionArr(): #
                if self.arr4List(): #
                    return True
            print('Error functionList()-1 => ',self.ts[self.index])
            return True 
        else:
            if self.ts[self.index][0] == ';':
                return True
        print('Error functionList()-2 => ',self.ts[self.index])
        return False
    
    def arr4List(self):
        if self.ts[self.index][0] in ['.','Assignment Operator', 'Increment/Decrement Operator']:
            if self.ts[self.index][0] == '.':
                print('Match arr4List()-1 => ',self.ts[self.index])
                self.index += 1
                if self.ts[self.index][0] == 'Identifier':
                    print('Match arr4List()-2 => ',self.ts[self.index])
                    self.index += 1
                    if self.arr4DOTList(): #
                        return True
            elif self.ts[self.index][0] == 'Assignment Operator':
                if self.assign(): #
                    return True
            elif self.ts[self.index][0] == 'Increment/Decrement Operator':
                if self.incDec():
                    return True
        else:
            if self.ts[self.index][0] == ';':
                return True
        print('Error arr4List() => ',self.ts[self.index])
        return False

    def arr4DOTList(self):
        if self.ts[self.index][0] in ['.','Assignment Operator','Increment/Decrement Operator','(','[']:
            if self.ts[self.index][0] == 'Assignment Operator':
                if self.assign(): #
                    return True
            elif self.ts[self.index][0] == 'Increment/Decrement Operator':
                if self.incDec():
                    return True
            elif self.ts[self.index][0] == '(':
                if self.functionCall():
                    return True
            elif self.ts[self.index][0] == '.':
                if self.objectCall():
                    return True
            elif self.ts[self.index][0] == '[':
                if self.arr4():
                    return True
        else:
            if self.ts[self.index][0] == ';':
                return True
        print('Error arr4DOTList() => ',self.ts[self.index])
        return False

    def functionList2(self): #checked
        if self.functionCall(): #
            return True
        elif self.assign(): #
            return True
        elif self.objectCall(): #
            return True
        elif self.arr4(): #
            return True
        elif self.incDec(): #
            return True
        print('Error functionList2() => ',self.ts[self.index])
        return False


    def objectCall(self):
        if self.ts[self.index][0] == '.':
            print('Match objectCall()-1 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == 'Identifier':
                print('Match objectCall()-2 => ',self.ts[self.index])
                self.index += 1
                if self.objectCallList(): #1342
                    return True
        print('Error objectCall() => ',self.ts[self.index])
        return False
    
    def arr4(self):
        if self.arr8(): #1361
            if self.arr4(): #1174
                return True
        print('Error arr4() => ',self.ts[self.index])
        return False
    
    def incDec(self): #checked
        if self.ts[self.index][0] == 'Increment/Decrement Opeartor':
            print('Match incDec() => ',self.ts[self.index])
            self.index += 1
            return True
        print('Error incDec() => ',self.ts[self.index])
        return False
    
    def param3(self):
        if self.ts[self.index][0] == ',':
            print('Match incDec() => ',self.ts[self.index])
            self.index += 1
            if self.param2(): #823
                return True
            print('Error param3()-1 => ',self.ts[self.index])
            return False
        elif self.ts[self.index][0] == ')':
            return True
        print('Error param3()-2 => ',self.ts[self.index])
        return False
    
    def arr(self): #checked
        if self.ts[self.index][0] == '[':
            print('Match arr() => ',self.ts[self.index])
            self.index += 1
            if self.arrList(): #1371
                return True
        print('Error arr() => ',self.ts[self.index])
        return False
    
    def obj(self): #checked
        if self.ts[self.index][0] == 'Identifier':
            print('Match obj() => ',self.ts[self.index])
            self.index += 1
            if self.allInit(): #386
                return True
        print('Error obj() => ',self.ts[self.index])
        return False
    
    def DTList(self):
        if self.ts[self.index][0] == 'Identifier':
            print('Match DTList() => ',self.ts[self.index])
            self.index += 1
            if self.allInit():
                return True
        elif self.arr5():
            return True
        print('Error DTList() => ',self.ts[self.index])
        return False
    
    def AE(self): #checked
        if self.RE(): #1275
            if self.AE_(): #1050
                return True
        print('Error AE() => ',self.ts[self.index])
        return False
    
    def incDecList(self):
        if self.ts[self.index][0] == 'Identifier':
            print('Match incDecList()-1 => ',self.ts[self.index])
            self.index += 1
            if self.incCall(): #1396
                return True
        elif self.ts[self.index][0] == 'This':
            print('Match incDecList()-2 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == '.':
                print('Match incDecList()-3 => ',self.ts[self.index])
                self.index += 1
                if self.ts[self.index][0] == 'Identifier':
                    print('Match incDecList()-4 => ',self.ts[self.index])
                    self.index += 1
                    if self.incCall(): #1396
                        return True
        print('Error incDecList() => ',self.ts[self.index])
        return False
    
    def chain(self):
        if self.ts[self.index][0] in ['(','.','[']:
            if self.ts[self.index][0] == '(':
                if self.functionCall3(): #1410
                    return True
            elif self.ts[self.index][0] == '.':
                if self.objectCall3(): #1423
                    return True
            elif self.ts[self.index][0] == '[':
                if self.arr3(): #1435
                    return True
            else:
                if self.ts[self.index][0] in ['Arithmetaic Operator','Relational Operator','Logical Operator', ';',')',',',']','}']:
                    return True
            print('Error chain() => ',self.ts[self.index])
            return False
        
    def RE(self): #checked
        if self.E(): #1282
            if self.RE_(): #1064
                return True
        print('Error RE() => ',self.ts[self.index])
        return False
    
    def E(self): #checked
        if self.T(): #1441
            if self.E_(): #1462
                return True
        print('Error E() => ',self.ts[self.index])
        return False
    
    def funcCallOE(self):
        if self.ts[self.index][0] == '(':
            print('Match funcCallOE()-1 => ',self.ts[self.index])
            self.index += 1
            if self.params(): #626
                if self.ts[self.index][0] == ')':
                    print('Match funcCallOE()-2 => ',self.ts[self.index])
                    self.index += 1
        print('Error funcCallOE() => ',self.ts[self.index])
        return False
         
    def objCallOE(self):
        if self.ts[self.index][0] == '.':
            print('Match funcCallOE()-1 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == 'Identifier':
                print('Match funcCallOE()-2 => ',self.ts[self.index])
                self.index += 1
                if self.OEList(): #1078
                    return True
        print('Error objCallOE() => ',self.ts[self.index])
        return False
    
    def ArrOE(self):
        if self.ts[self.index][0] == '[':
            print('Match ArrOE() => ',self.ts[self.index])
            self.index += 1
            if self.OE(): #936
                if self.arrOEList(): #1476
                    return True
        print('Error ArrOE() => ',self.ts[self.index])
        return False
    
    def arrConst(self):
        if self.OE(): #936
            if self.ACL(): #1491
                return True
        print('Error arrConst() => ',self.ts[self.index])
        return False
    
    def arrConst3(self):
        if self.ts[self.index][0] == '{':
            print('Match arrConst3()-1 => ',self.ts[self.index])
            self.index += 1
            if self.arrConst0(): #1114
                if self.ts[self.index][0] == '}':
                    print('Match arrConst3()-2 => ',self.ts[self.index])
                    self.index += 1
                    if self.arrConst4(): #1505
                        return True
        print('Error arrConst3() => ',self.ts[self.index])
        return False
    
    def objectCallList(self): #checked
        if self.ts[self.index][0] == '.':
            if self.objectCall(): #1162
                return True
        elif self.ts[self.index][0] == '(':
            if self.functionCall(): #1150
                return True
        elif self.ts[self.index][0] == 'Assignment Operator':
            if self.assign(): #482
                return True
        elif self.ts[self.index][0] == '[':
            if self.arr4(): #1174
                return True
        elif self.ts[self.index][0] == 'Increment/Decrement Opeartor':
            if self.incDec(): #1181
                return True
        print('Error objectCallList() => ',self.ts[self.index])
        return False
    
    def arr8(self):
        if self.ts[self.index][0] == '[':
            print('Match arr8() => ',self.ts[self.index])
            self.index += 1
            if self.OE(): #936
                if self.arr8List(): #1571
                    return True
        print('Error arr8() => ',self.ts[self.index])
        return False
    
    def arrList(self): #checked
        if self.ts[self.index][0] == ']':
            print('Match arrList()-1 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == 'Identifier':
                print('Match arrList()-2 => ',self.ts[self.index])
                self.index += 1
                if self.allInit(): #386
                    return True
        elif self.ts[self.index][0] == ',':
            print('Match arrList()-3 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == ']':
                print('Match arrList()-4 => ',self.ts[self.index])
                self.index += 1
                if self.ts[self.index][0] == 'Identifier':
                    print('Match arrList()-2 => ',self.ts[self.index])
                    self.index += 1
                    if self.allInit(): #386
                        return True
        elif self.OE(): #936
            if self.arrFunList(): #
                return True
        print('Error arrList() => ',self.ts[self.index])
        return False
    
    def arrFunList(self): #checked
        if self.ts[self.index][0] == ']':
            print('Match arrFunList()-1 => ',self.ts[self.index])
            self.index += 1
            if self.ARLF(): #
                return True
        elif self.ts[self.index][0] == ',':
            print('Match arrFunList()-2 => ',self.ts[self.index])
            self.index += 1
            if self.OE(): #
                if self.ts[self.index][0] == ']':
                    print('Match arrFunList()-3 => ',self.ts[self.index])
                    self.index += 1
                    if self.ARLF(): #
                        return True
        print('Error arrFunList() => ',self.ts[self.index])
        return False

    def ARLF(self): #checked
        if self.ts[self.index][0] == '.':
            print('Match ARLF()-1 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == 'Identifier':
                print('Match ARLF()-2 => ',self.ts[self.index])
                self.index += 1
                if self.DOTList(): #
                    return True
        elif self.assign(): #
            return True
        elif self.incDec(): #
            return True
        print('Error ARLF() => ',self.ts[self.index])
        return False

    def DOTList(self): #checked
        if self.ts[self.index][0] == '(':
            if self.functionCall(): #
                return True
        elif self.ts[self.index][0] == '.':
            if self.objectCall(): #
                return True
        elif self.ts[self.index][0] == '[':
            if self.arr4(): #
                return True
        elif self.ts[self.index][0] == 'Assignment Operator':
            if self.assign(): #
                return True
        elif self.ts[self.index][0] == 'Increment/Decrement Operator':
            if self.incDec(): #
                return True
        print('Error DOTList() => ',self.ts[self.index])
        return False

    def arr2(self): #checked
        if self.ts[self.index][0] == '[':
            print('Match arr2() => ',self.ts[self.index])
            self.index += 1
            if self.OE(): #
                if self.arr2List():
                    return True
        print('Error arr2() => ',self.ts[self.index])
        return False

    def arr2List(self): #checked
        if self.ts[self.index][0] == ']':
            print('Match arr2List()-1 => ',self.ts[self.index])
            self.index += 1
            if self.arr2CL(): #
                return True
        elif self.ts[self.index][0] == ',':
            print('Match arr2List()-2 => ',self.ts[self.index])
            self.index += 1
            if self.OE(): #
                if self.ts[self.index][0] == ']':
                    print('Match arr2List()-3 => ',self.ts[self.index])
                    self.index += 1
                    if self.arr2CL(): #
                        return True
        print('Error arr2List() => ',self.ts[self.index])
        return False

    def arr2CL(self): #checked
        if self.ts[self.index][0] == '.':
            print('Match arr2CL()-1 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == 'Identifier':
                print('Match arr2CL()-2 => ',self.ts[self.index])
                self.index += 1
                if self.arr2CLList(): #
                    return True
            print('Error arr2CL()-1 => ',self.ts[self.index])
            return False
        if self.incDec(): #
            return True
        if self.assign2():#
            return True
        if self.ts[self.index][0] == ';':
            return True
        print('Error arr2CL()-2 => ',self.ts[self.index])
        return False

    def arr2CLList(self): #checked
        if self.functionCall(): #
            return True
        elif self.arr(): #
            return True
        elif self.objectCall(): #
            return True
        if self.incDec():
            return True
        print('Error arr2CLList() => ',self.ts[self.index])
        return False

    """ def objectCall(self): #checked
        if self.ts[self.index][0] == '.':
            print('Match objectCall()-1 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == 'Identifier':
                print('Match objectCall()-2 => ',self.ts[self.index])
                self.index += 1
                if self.objectCallList():
                    return True
        print('Error objectCall() => ',self.ts[self.index])
        return False """

    def assign2(self): #checked
        if self.assign(): #
            return True
        if self.ts[self.index][0] == ';':
            return True
        print('Error assign2() => ',self.ts[self.index])
        return False

    def incCall(self):
        if self.ts[self.index][0] == '(' or self.ts[self.index][0] == '[':
            if self.ts[self.index][0] == '(':
                if self.functionCall3(): #1396
                    return True
            elif self.ts[self.index][0] == '[':
                if self.arr3(): #1435
                    return True
            else:
                if self.ts[self.index][0] in ['Arithmetaic Operator','Relational Operator','Logical Operator', ';',')',',',']']:
                    return True
            print('Error incCall() => ',self.ts[self.index])
            return False
        
    def functionCall3(self):
        if self.ts[self.index][0] == '(':
            print('Match functionCall3()-1 => ',self.ts[self.index])
            self.index += 1
            if self.params(): #626
                if self.ts[self.index][0] == ')':
                    print('Match functionCall3()-2 => ',self.ts[self.index])
                    self.index += 1
                    if self.function3List(): #1532
                        return True
        print('Error functionCall3() => ',self.ts[self.index])
        return False
    
    def objectCall3(self):
        if self.ts[self.index][0] == '.':
            print('Match objectCall3()-1 => ',self.ts[self.index])
            self.index += 1
            if self.ts[self.index][0] == 'Identifier':
                print('Match objectCall3()-2 => ',self.ts[self.index])
                self.index += 1
                if self.chain(): #1258
                    return True
        print('Error objectCall3() => ',self.ts[self.index])
        return False
    
    def arr3(self):
        if self.arr8(): #1361
            return True
        print('Error arr3() => ',self.ts[self.index])
        return False
             
    def T(self): #checked
        if self.F(): #976
            if self.T_(): #1443
                return True
        print('Error T() => ',self.ts[self.index])
        return False
    
    def T_(self): #checked
        if self.ts[self.index][0] == 'Arithmetaic Operator':
            print('Match T_() => ',self.ts[self.index])
            self.index += 1
            if self.F(): #976
                if self.T_(): #1448
                    return True
            print('Error T_()-1 => ',self.ts[self.index])
            return False
        elif self.ts[self.index][0] in ['Arithmetaic Operator','Relational Operator','Logical Operator', ';',')',',',']','}']:
            return True
        print('Error T_()-2 => ',self.ts[self.index])
        return False
    
    def E_(self): #checked
        if self.ts[self.index][0] == 'Arithmetaic Operator':
            print('Match E_() => ',self.ts[self.index])
            self.index += 1
            if self.T(): #1441
                if self.E_(): #1448
                    return True
            print('Error E_()-1 => ',self.ts[self.index])
            return False
        elif self.ts[self.index][0] in ['Arithmetaic Operator','Relational Operator','Logical Operator', ';',')',',',']','}']:
            return True
        print('Error E_()-2 => ',self.ts[self.index])
        return False
    
    def arrOEList(self):
        if self.ts[self.index][0] == ']':
            print('Match arrOEList()-1 => ',self.ts[self.index])
            self.index += 1
            if self.arrOEValue(): #1559
                return True
        elif self.ts[self.index][0] == ',':
            print('Match arrOEList()-2 => ',self.ts[self.index])
            self.index += 1
            if self.OE(): #936
                if self.arrOEValue(): #1559
                    return True
        print('Error arrOEList() => ',self.ts[self.index])
        return False
    
    def ACL(self):
        if self.ts[self.index][0] == ',':
            print('Match ACL()-1 => ',self.ts[self.index])
            self.index += 1
            if self.arrConst(): #1322
                return True
            print('Error ACL()-1 => ',self.ts[self.index])
            return False
        else:
            if self.ts[self.index][0] == '}':
                return True
        print('Error ACL()-2 => ',self.ts[self.index])
        return False
    
    def arrConst4(self):
        if self.ts[self.index][0] == ',':
            print('Match arrConst4() => ',self.ts[self.index])
            self.index += 1
            if self.arrConst3(): #1329
                return True
        else:
            if self.ts[self.index][0] == '}':
                return True
        print('Error arrConst4() => ',self.ts[self.index])
        return False
    
    def arr8List(self):
        if self.ts[self.index][0] == ']':
            print('Match arr8List()-1 => ',self.ts[self.index])
            self.index += 1
            return True
        elif self.ts[self.index][0] == ',':
            print('Match arr8List()-2 => ',self.ts[self.index])
            self.index += 1
            if self.OE(): #936
                if self.ts[self.index][0] == ']':
                    print('Match arr8List()-3 => ',self.ts[self.index])
                    self.index += 1
        print('Error arr8List() => ',self.ts[self.index])
        return False
    
    def function3List(self):
        if self.ts[self.index][0] == '[' or self.ts[self.index][0] == '.':
            if self.ts[self.index][0] == '.':
                print('Match function3List()-1 => ',self.ts[self.index])
                self.index += 1
                if self.ts[self.index][0] == 'Identifier':
                    print('Match function3List()-2 => ',self.ts[self.index])
                    self.index += 1
                    if self.chain(): #1258
                        return True
            elif self.functionArr(): #1577
                if self.ts[self.index][0] == '.':
                    print('Match function3List()-3 => ',self.ts[self.index])
                    self.index += 1
                    if self.ts[self.index][0] == 'Identifier':
                        print('Match function3List()-4 => ',self.ts[self.index])
                        self.index += 1
                        if self.chain(): #1258
                            return True
                else:
                    if self.ts[self.index][0] == ';' or self.ts[self.index][0] == ',':
                        return True
            print('Error function3List()-1 => ',self.ts[self.index])
            return False
        print('Error function3List()-2 => ',self.ts[self.index])
        return False
    
    def arrOEValue(self):
        if self.ts[self.index][0] == '.' or self.ts[self.index][0] == 'Increment/Decrement Opeartor':
            if self.ts[self.index][0] == '.':
                print('Match arrOEValue()-1 => ',self.ts[self.index])
                self.index += 1    
                if self.ts[self.index][0] == 'Identifier':
                    print('Match arrOEValue()-2 => ',self.ts[self.index])
                    self.index += 1  
                    if self.OEList(): #1078
                        return True
            elif self.incDec(): #1181
                return True
        else:
            if self.ts[self.index][0] in ['Arithmetaic Operator','Relational Operator','Logical Operator', ';',')',',',']']:
                return True
        print('Error arrOEValue() => ',self.ts[self.index])
        return False
    
    def functionArr(self):
        if self.ts[self.index][0] == '[':
            print('Match functionArr() => ',self.ts[self.index])
            self.index += 1 
            if self.OE(): #936
                if self.functionArrList(): #1587
                    return True
        print('Error functionArr() => ',self.ts[self.index])
        return False
    
    def functionArrList(self):
        if self.ts[self.index][0] == ']':
            print('Match functionArrList()-1 => ',self.ts[self.index])
            self.index += 1 
            return True
        elif self.ts[self.index][0] == ',':
            print('Match functionArrList()-2 => ',self.ts[self.index])
            self.index += 1 
            if self.OE(): #936
                if self.ts[self.index][0] == ']':
                    print('Match functionArrList()-3 => ',self.ts[self.index])
                    self.index += 1 
                    return True
        print('Error functionArrList() => ',self.ts[self.index])
        return False

    def MF(self):
        if self.ts[self.index][0] == 'Identifier':
            print('Match MF() => ',self.ts[self.index])
            self.index += 1 
            if self.AMList3(): #
                return True
        else:
            if self.ts[self.index][0] in ['}','Arithmetaic Operator','Static','Virtual/Override','Identifier','Abstract','Class','Interface']:
                return True
        print('Error MF() => ',self.ts[self.index])
        return False
    
    def AMList3(self):
        if self.ts[self.index][0] == 'Arithmetaic Operator' or self.ts[self.index][0] == ';':
            if self.allInit(): #
                if self.ts[self.index][0] == ';':
                    print('Match AMList3() => ',self.ts[self.index])
                    self.index += 1 
                    return True
        elif self.ts[self.index][0] == '(':
            if self.method(): #
                return True 
        # print('Error AMList3() => ',self.ts[self.index])Error Error 
        return False

    def arr5(self):
        if self.ts[self.index][0] == '[':
            print('Match arr5() => ',self.ts[self.index])
            self.index += 1 
            if self.arr5List(): #
                return True
        # print('Error arr5() => ',self.ts[self.index])
        return False

    def arr5List(self):
        if self.ts[self.index][0] == ']':
            print('Match arr5List()-1 => ',self.ts[self.index])
            self.index += 1 
            if self.ts[self.index][0] == 'Identifier':
                print('Match arr5List()-2 => ',self.ts[self.index])
                self.index += 1 
                if self.allInit(): #
                    return True
        elif self.ts[self.index][0] == ',':
            print('Match arr5List()-3 => ',self.ts[self.index])
            self.index += 1 
            if self.ts[self.index][0] == ']':
                print('Match arr5List()-4 => ',self.ts[self.index])
                self.index += 1 
                if self.ts[self.index][0] == 'Identifier':
                    print('Match arr5List()-5 => ',self.ts[self.index])
                    self.index += 1 
                    if self.allInit(): #
                        return True
        # print('Error arr5List() => ',self.ts[self.index])
        return False