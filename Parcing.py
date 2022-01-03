import time
start_time= time.time()
def tags(text):
    i=0
    lenght=len(text)
    out=[]
    while i<lenght:
        while i<lenght and text[i]!='<':
            i+=1
        i+=1
        start=i
        while i<lenght and text[i]!='>':
                i+=1
        end=i
        tag=text[start:end]
        if tag!='':
            out.append(tag)
        while 1+i+len(tag)<lenght and text[i:1+i+len(tag)]!='/'+tag:
            i+=1
    return out
def stack(text):
    tag=tags(text)
    if tag==[]:
        if text.isdigit():  
            text=int(text)
        return text
    else:
        m={}
        i=0
        for k in tag:
            while i+len(k)+2<len(text) and text[i:i+len(k)+2]!='<'+k+'>':
                i+=1
            i+=len(k)+2
            start=i
            while i+len(k)+3<len(text) and text[i:i+len(k)+3]!='</'+k+'>':
                i+=1
            end=i
            if k in m.keys():
                m[k].append(stack(text[start:end]))
            else:
                m[k]=[stack(text[start:end])]
        for k in tag:
            if len(m[k])==1:
                m[k]=m[k][0]
        return m
with open('lab4_rasp.txt','r', encoding="utf8") as input_file:
    text=input_file.read()
out=str(stack(text))
out=out.replace("'", '"')
print(out)
print("--- %s seconds ---" % (time.time() - start_time))