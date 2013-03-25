class tail_reverse:
    def read1(self,file):
        self.f=file
	fd=open(self.f,'r')
	txt=fd.read()
	return txt
class main(tail_reverse):
    def method(self,file,no_lines):
	data=tail_reverse.read1(self,file)
	lst=data.splitlines()
	lines_in_file=len(lst)
	lines=no_lines
	count=0
        result=[]
	for i in lst:
            if count<lines_in_file-lines:
	        count+=1
            else:
                 result.insert(0,i)
        for i in result:
            print i
	        
			  
a=main()
a.method('reverse.txt',5)	
