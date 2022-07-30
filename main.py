#-------------MODULES IMPORTED---------------

from tkinter import *
import ctypes
from PIL import Image,ImageTk
import random


#--------CLASS DEFINITION----------
class Railway(object):
    def __init__(self):
        pass

#----------------MAIN LOOP-------------
def main():
    pwd.destroy()
    root=Tk()
    root.title('Indian Railways')

    #------GEOMETRY OF MAIN LOOP---------
    user32=ctypes.windll.user32
    sz_x=user32.GetSystemMetrics(0)
    sz_y=user32.GetSystemMetrics(1)
    root_x=650
    root_y=650
    ad_x=int((sz_x-root_x)/2)
    ad_y=int((sz_y-root_y)/2)
    size=str(root_x)+'x'+str(root_y)+'+'+str(ad_x)+'+'+str(ad_y)
    root.geometry(size)
    root.resizable(0,0)
    root.configure(background="#E7E8D1")

    # background_image = PhotoImage(file=r'D:\projects\railway\PHOTOS\welcome.png')

    # background = Label(root, image=background_image)
    # background.place(x=0,y=0,relheight=1,relwidth=1)
    # background.pack()

    #--------PRIMARY FRAME-----------

    def FRM1():
        global frm1
        frm1=Frame(root,bg="#A7BEAE")
        frm1.pack()


        #------FRAME ADDITION TO ROOT WINDOW-------
        frmS=Frame(root)
        frmP=Frame(root)
        frmT=Frame(root)
        frmG=Frame(root)
        fm=Frame(root)
        tkt=Frame(root)
        frmH=Frame(root)
        
        # frmS.configure(background="#A7BEAE")
        # frmP.configure(background="#A7BEAE")
        # frmT.configure(background="#A7BEAE")
        # frmG.configure(background="#A7BEAE")
        # fm.configure(background="#A7BEAE")
        # tkt.configure(background="#A7BEAE")
        # frmH.configure(background="#A7BEAE")
        


        #-----------BUTTONS AND LABELS---------
        lb1=Label(frm1,text='\nWELCOME TO INDIAN RAILWAYS:\n\n',bg="#A7BEAE",font=('Ariel','22'))
        lb1.pack()
        bt1=Button(frm1,text='Search Trains',bg='#E59866',fg='white',height=3,width=25,command=lambda :FRMS())
        bt1.pack()
        bt2=Button(frm1,text='PNR Enquiry',bg='#E59866',fg='white',height=3,width=25,command=lambda:FRMP())
        bt2.pack()
        bt3=Button(frm1,text='Get Train Schedule',bg='#E59866',fg='white',height=3,width=25,command=lambda:FRMT())
        bt3.pack()
        bt4=Button(frm1,text='Ticket Booking',bg='#E59866',fg='white',height=3,width=25,command=lambda:FRMG())
        bt4.pack()
        bt5=Button(frm1,text='HELP',bg='#E59866',fg='white',height=3,width=25,command=lambda:FRMH())
        bt5.pack()

        #-----------SECONDARY FRAMES----------

        ##----------SECONDARY FRAME 1-----------
        def FRMS():
            frm1.destroy()
            
            global frmS
            frmS=Frame(root,bg="#A7BEAE")
            frmS.pack()

            #----------LABEL BUTTONS AND ENTRIES----------
            back_button(frmS)
            lb1=Label(frmS,text='\nFROM STATION (name or code):',bg="#A7BEAE")
            lb1.pack()
            en1=Entry(frmS)
            en1.pack()
            lb2=Label(frmS,text='\nTO STATION (name or code):',bg="#A7BEAE")
            lb2.pack()
            en2=Entry(frmS)
            en2.pack()
            lb3=Label(frmS,bg="#A7BEAE")
            lb3.pack()
            bt1=Button(frmS,text='GO',bg='#E59866',fg='white',height=1,width=7,\
                       command=lambda x=en1,y=en2:searchTBS(x,y))
            bt1.pack()

            #------------SEARCH FUNCTION-------------
            def searchTBS(a1,a2):
                a1=a1.get().strip().upper()
                a2=a2.get().strip().upper()
                fin=open(r'D:\projects\railway\STATION CODE\STATION CODE.txt','r')
                abc=fin.read()
                if a1 in abc and a2 in abc and a1!='' and a2!='':
                    fin.seek(0)
                    i=fin.readline()
                    counter=0
                    while i:
                        i=i.strip('\n()')
                        l=i.split(',')
                        if (a1==l[0] or a1==l[1]):
                            if a1==l[1]:
                                a1=l[0]
                            counter+=1
                        if (a2==l[0] or a2==l[1]):
                            if a2==l[1]:
                                a2=l[0]
                            counter+=1
                        if counter==2:
                            break
                        else:
                            i=fin.readline()
                    else:
                        frmS.destroy()
                        FRMS()
                        txt='NOT FOUND! TRY AGAIN OR SEE HELP'
                        lb=Label(frmS,text=txt,bg="#A7BEAE")
                        lb.pack()
                        return
                    search(a1,a2)
                else:
                    frmS.destroy()
                    FRMS()
                    txt='\nNOT FOUND! TRY AGAIN OR SEE HELP'
                    lb=Label(frmS,text=txt,bg="#A7BEAE")
                    lb.pack()

            def search(a1,a2):
                TR=[10103,12553,12565,16176]
                p=[]
                for m in TR:
                    path=r'D:\projects\railway\TRAINS\%s.txt'%str(m)
                    fout=open(path,'r')
                    abc=fout.read()
                    if a1 in abc and a2 in abc:
                        fout.seek(0)
                        y=fout.readline();y=y.strip('\n')
                        z=fout.readline();z=z.strip('\n')
                        fout.seek(0)
                        c=fout.readlines()
                        for s in range(len(c)):
                            if c[s]=='STATIONS\n':
                                begin=s+1
                            elif c[s]=='SEATS\n':
                                end=s
                        rslt=c[begin:end]
                        for q in rslt:
                            a=q.strip('\n()')
                            a=a.split(',')
                            if a1==a[1].strip("'"):
                                s1=int(a[0])
                            if a2==a[1].strip("'"):
                                s2=int(a[0])
                
                        if s1-s2<0:
                            p.append([y,z])
                if p==[]:
                    frmS.destroy()
                    FRMS()
                    txt='\nNo Train Found Between The Stations'
                    lb=Label(frmS,text=txt,bg="#A7BEAE")
                    lb.pack()
                else:
                    frmS.destroy()
                    FRMS()
                    tx=Text(frmS)
                    tx.insert(INSERT,'\nAVAILABLE TRAINS ARE:\n\nTRAIN NO\t\tTRAIN NAME')
                    for k in p:
                        a=k[0].strip("'")
                        b=k[1].strip("'")
                        txt='\n'+a+'\t\t'+b
                        tx.insert(INSERT,txt)
                        tx.pack()

        ##----------SECONDARY FRAME 2-----------
        def FRMP():
            frm1.destroy()
            
            global frmP
            frmP=Frame(root,bg="#A7BEAE")
            frmP.pack()

            #----------LABEL BUTTONS AND ENTRIES----------
            back_button(frmP)
            lb1=Label(frmP,text='\n10-DIGIT PNR NUMBER:',bg="#A7BEAE")
            lb1.pack()
            en1=Entry(frmP)
            en1.pack()
            bt1=Button(frmP,text='Find Details',bg='#E59866',fg='white',command=lambda x=en1:check(x))
            bt1.pack()

            #------------FIND DETAILS USING PNR---------------
            def check(a):
                a=a.get().strip()
                if a!='':
                    fin=open(r'D:\projects\railway\PNRS\PNRS.txt','r')
                    i=fin.readline()
                    while i:
                        p=i.strip('\n')
                        if a==i:
                            show(i)
                            break
                        else:
                            i=fin.readline()
                    else:
                        frmP.destroy()
                        FRMP()
                        lb=Label(frmP,text='\n\nINVALID PNR!!!',bg="#A7BEAE")
                        lb.pack()
                else:
                    frmP.destroy()
                    FRMP()
                    lb=Label(frmP,text='\n\nINVALID PNR!!!',bg="#A7BEAE")
                    lb.pack()
            def show(a):
                fin=open(r'D:\projects\railway\PASSENGER\PASSENGER.txt','r')
                i=fin.readline()
                while i:
                    ls=i.split(',')
                    if a==ls[0]:
                        h=ls
                        break
                    else:
                        i=fin.readline()


                txt='\nHERE ARE THE DETAILS OF BOOKINGS\n'
                txt=txt+'\nPNR NO: '+h[0]
                txt=txt+'\nPASSENGER\'S NAME: '+h[1]
                txt=txt+'\nAGE: '+h[3]
                txt=txt+'\nGENDER: '+h[4]
                txt=txt+'\nRESERVED ON: '+h[9]
                txt=txt+'\nNO OF SEATS: '+h[2]
                txt=txt+'\nTRAIN NO: '+h[5]
                txt=txt+'\nTRAIN NAME: '+conv1(h[5])
                txt=txt+'\nFROM STATION: '+conv(h[6])
                txt=txt+'\nTO STATION: '+conv(h[7])
                txt=txt+'\nCLASS: '+h[8]
                frmP.destroy()
                FRMP()
                t=Text(frmP)
                t.insert(INSERT,txt)
                t.pack()
                
                

        ##----------SECONDARY FRAME 3-----------
        def FRMT():
            frm1.destroy()
            global frmT
            frmT=Frame(root,bg="#A7BEAE")
            frmT.pack()

            #----------LABEL BUTTONS AND ENTRIES----------
            back_button(frmT)
            lb1=Label(frmT,text='\nTRAIN NUMBER:',bg="#A7BEAE")
            lb1.pack()
            en1=Entry(frmT)
            en1.pack()
            lb2=Label(frmT,text='OR\n\nTRAIN NAME:',bg="#A7BEAE")
            lb2.pack()
            en2=Entry(frmT)
            en2.pack()
            lb3=Label(frmT,bg="#A7BEAE")
            lb3.pack()
            bt1=Button(frmT,text='Get Schedule',bg='#E59866',fg='white',command=lambda x=en1,y=en2:getsch(x,y))
            bt1.pack()
            

            #--------GET SCHEDULE FUNCTION-----------
            def getsch(a1,a2):
                a1=a1.get().strip().upper()
                a2=a2.get().strip().upper()
                fin=open(r'D:\projects\railway\TRAIN CODE\TRAIN CODE.txt','r')
                abc=fin.read()
                if a1 in abc or a2 in abc and (a1!='' or a2!=''):
                    fin.seek(0)
                    i=fin.readline()
                    while i:
                        i=i.strip('\n()')
                        l=i.split(',')
                        if a1 == l[0] or a2 ==l[1]:
                            code=l[0]
                            path=r'D:\projects\railway\TRAINS\%s.txt'%str(code)
                            fout=open(path,'r')
                            m=fout.readlines()
                            for c in range(len(m)):
                
                                if m[c]=='STATIONS\n':
                                    begin=c+1
                                elif m[c]=='SEATS\n':
                                    end=c
                            rslt=m[begin:end]
                            fout.seek(0)
                            
                            txt='\nINFORMATION:\n\n'
                            a=fout.readline().strip('\n')
                            txt=txt+'TRAIN NO: '+a+'\n'
                            a=fout.readline().strip('\n')
                            txt=txt+'TRAIN NAME: '+a+'\n'
                            a=fout.readline().strip('\n')
                            txt=txt+'SOURCE: '+conv(a)+'\n'
                            a=fout.readline().strip('\n')
                            txt=txt+'DESTINATION: '+conv(a)+'\n'
                            a=fout.readline().strip('\n()')
                            txt=txt+'RUNDAYS: '+a+'\n'
                            a=fout.readline().strip('\n()')
                            txt=txt+'CLASSES: '+a+'\n'
                            a=fout.readline().strip('\n')
                            txt=txt+'AVERAGE SPEED: '+a+' KMPH\n\n'
                            txt=txt+'TIME TABLE:\n\n'
                            txt=txt+'#\tSTATION\t\tARRIVAL\tDEPARTURE\t\tDAY\tDIST'
                            frmT.destroy()
                            FRMT()
                            tx=Text(frmT)
                            tx.insert(INSERT,txt)

                            
                            for q in rslt:
                                l=q.strip('\n()').split(',')
                                a=l[0]
                                txt='\n'+a+'\t'
                                b=l[1].strip("'")
                                txt=txt+conv(b)+'\t\t'
                                c=l[2].strip("'").replace("-",":")
                                txt=txt+c+'\t'
                                d=l[3].strip("'").replace("-",":")
                                txt=txt+d+'\t\t'
                                e=l[4]
                                txt=txt+e+'\t'
                                f=l[5]
                                txt=txt+f
                                tx.insert(INSERT,txt)
                                tx.pack()
                                
                            return
                        
                        else:
                            i=fin.readline()
                    else:
                        frmT.destroy()
                        FRMT()
                        txt='\nNOT FOUND! TRY AGAIN OR SEE HELP'
                        lb=Label(frmT,text=txt,bg="#A7BEAE")
                        lb.pack()
                else:
                    frmT.destroy()
                    FRMT()
                    txt='\nNOT FOUND! TRY AGAIN OR SEE HELP'
                    lb=Label(frmT,text=txt,bg="#A7BEAE")
                    lb.pack()

        ##----------SECONDARY FRAME 4-----------
        def FRMG():
            frm1.destroy()
            
            global frmG
            frmG=Frame(root,bg="#A7BEAE")
            frmG.pack()
            global fm
            fm=Frame(root,bg="#A7BEAE")
            fm.pack()
            

            #----------LABEL BUTTONS AND ENTRIES----------
            back_button(frmG,fm)
            lb1=Label(frmG,text='\nTRAIN NUMBER:',bg="#A7BEAE")
            lb1.pack()
            en1=Entry(frmG)
            en1.pack()
            lb2=Label(frmG,text='OR\n\nTRAIN NAME:',bg="#A7BEAE")
            lb2.pack()
            en2=Entry(frmG)
            en2.pack()
            lb3=Label(frmG,text='\nDATE:\n',bg="#A7BEAE")
            lb3.pack()
            lb4=Label(frmG,text='DD',bg="#A7BEAE")
            lb4.pack(side=LEFT)
            en3=Entry(frmG,width=5)
            en3.pack(side=LEFT)
            lb5=Label(frmG,text='MM',bg="#A7BEAE")
            lb5.pack(side=LEFT)
            en4=Entry(frmG,width=5)
            en4.pack(side=LEFT)
            lb6=Label(frmG,text='YYYY',bg="#A7BEAE")
            lb6.pack(side=LEFT)
            en5=Entry(frmG,width=8)
            en5.pack(side=LEFT)
            bt1=Button(frmG,text='Get Availablity',bg='#E59866',fg='white',command=lambda x=en1,\
                       y=en2,z=en3,x1=en4,y1=en5:avail(x,y,z,x1,y1))
            bt1.pack()

            

            #--------TRAIN AVAILABILITY FUNCTION-----------
            def avail(a1,a2,a3,a4,a5):
                a1=a1.get().strip().upper()
                a2=a2.get().strip().upper()
                a3=a3.get().strip()
                a4=a4.get().strip()
                a5=a5.get().strip()
                l=checkavail(a1,a2,a3,a4,a5)
                
                if l:
                    fwd=0
                    for i in l[0]:
                        if i:
                            fwd=1
                            break
                    if fwd==0:
                        txt='\nSEAT UNAVAILABLE FOR THE REQUESTED DATE'
                        frmG.destroy()
                        fm.destroy()
                        FRMG()
                        tx=Text(fm)
                        tx.insert(INSERT,txt)
                        tx.pack()
                        return
                    else:
                        txt='\nAvailable Seats:\n\nCOACH AC1: '+str(l[0][0])+'\n'
                        txt=txt+'COACH AC2: '+str(l[0][1])+'\n'
                        txt=txt+'COACH AC3: '+str(l[0][2])+'\n'
                        txt=txt+'COACH SLEEPER: '+str(l[0][3])

                        frmG.destroy()
                        fm.destroy()
                        FRMG()
                        btn=Button(fm,text='CONTINUE BOOKING',bg='#E59866',fg='white',\
                                   command=lambda x=a1,y=a2,z=a3,x1=a4,x2=a5,x3=l:\
                                   TKT(x,y,z,x1,x2,x3))
                        btn.pack()
                        tx=Text(fm)
                        tx.insert(INSERT,txt)
                        tx.pack()
                else:
                    frmG.destroy()
                    fm.destroy()
                    FRMG()
                    lb=Label(fm,text='\nINVALID ENTRY!!!\nENTER CORRECT DATA',bg="#A7BEAE")
                    lb.pack()
                    
                    

            def checkavail(a1,a2,a3,a4,a5):
                fin=open(r'D:\projects\railway\TRAIN CODE\TRAIN CODE.txt','r')
                abc=fin.read()
                
                if (a1 in abc or a2 in abc) and a3!='' and a4!='' and a5!='' and (a1!='' or a2!=''):
                    fin.seek(0)
                    i=fin.readline()
                    while i:
                        i=i.strip('\n()')
                        l=i.split(',')
                        if a1 == l[0] or a2 ==l[1]:
                            code=l[0]
                            path=r'D:\projects\railway\TRAINS\%s.txt'%str(code)
                            fout=open(path,'r')
                            m=fout.readlines()
                            for c in range(len(m)):
                                if m[c]=='SEATS\n':
                                    beg1=c+1
                                elif m[c]=='RESERVATION\n':
                                    end1=c
                                    beg2=c+1
                            seats=m[beg1:end1]
                            rsrv=m[beg2:]
                            ct=0
                            dt=str(a3)+'-'+str(a4)+'-'+str(a5)
                            for s in rsrv:
                                if dt in s:
                                    ast=s
                                    ct=1
                                    break
                            if ct==0:
                                gs1=int((seats[0]).strip('\n()').split(',')[1])
                                gs2=int((seats[1]).strip('\n()').split(',')[1])
                                gs3=int((seats[2]).strip('\n()').split(',')[1])
                                gs4=int((seats[3]).strip('\n()').split(',')[1])
                                return [[gs1,gs2,gs3,gs4],[0,0,0,0]]
                            else:
                    
                                ast=str(ast)
                                ast=ast.strip('\n()')
                                ast=ast.split(',')
                                rs1=int(ast[1][3:])
                                rs2=int(ast[2][3:])
                                rs3=int(ast[3][3:])
                                rs4=int(ast[4][3:])
                                gs1=int((seats[0]).strip('\n()').split(',')[1])
                                gs2=int((seats[1]).strip('\n()').split(',')[1])
                                gs3=int((seats[2]).strip('\n()').split(',')[1])
                                gs4=int((seats[3]).strip('\n()').split(',')[1])
                                return [[gs1-rs1,gs2-rs2,gs3-rs3,gs4-rs4],[rs1,rs2,rs3,rs4]]
                        else:
                            i=fin.readline()

                    else:
                        return []
            
                else:
                    return []

            #-----------TICKET BOOKING FRAME---------
            def TKT(a1,a2,a3,a4,a5,a6):
                frmG.destroy()
                fm.destroy()
                frm1.destroy()
                global tkt
                tkt=Frame(root,bg="#A7BEAE")
                
                tkt.pack()

                #----------LABEL BUTTONS AND ENTRIES----------
                b0=Button(tkt,text='BACK',bg='#E59866',fg='white',height=1,width=7,command=lambda:rest())
                b0.pack()
                def rest():
                    tkt.destroy()
                    FRMG()
                lb1=Label(tkt,text='Passanger\'s Name:',bg="#A7BEAE")
                lb1.pack()
                en1=Entry(tkt)
                en1.pack()
                lb2=Label(tkt,text='Passenger\'s Age:',bg="#A7BEAE")
                lb2.pack()
                en3=Entry(tkt)
                en3.pack()
                lb=Label(tkt,text='No. Of Seats To Be Booked:',bg="#A7BEAE")
                lb.pack()
                en2=Entry(tkt)
                en2.pack()
                lb3=Label(tkt,text='Gender (M/F):',bg="#A7BEAE")
                lb3.pack()
                en4=Entry(tkt)
                en4.pack()
                lb6=Label(tkt,text='FROM STATION (name or code):',bg="#A7BEAE")
                lb6.pack()
                en6=Entry(tkt)
                en6.pack()
                lb7=Label(tkt,text='TO STATION (name or code):',bg="#A7BEAE")
                lb7.pack()
                en7=Entry(tkt)
                en7.pack()
                lb8=Label(tkt,text='CLASS (1A/2A/3A/SL):',bg="#A7BEAE")
                lb8.pack()
                en8=Entry(tkt)
                en8.pack()
                bt1=Button(tkt,text='Proceed',bg='#E59866',fg='white',command=lambda x=en1,y=en2,z=en3,\
                           x1=en4,x2=a1,x3=en6,x4=en7,x5=en8,s=a3,t=a4,u=a5,v=a2,w=a6:\
                           book(x,y,z,x1,x2,x3,x4,x5,s,t,u,v,w))
                bt1.pack()

                #--------TICKET BOOKING FUNCTION----------
                def book(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13):
                    
                    a1=a1.get().strip().upper()
                    a2=a2.get().strip()
                    a3=a3.get().strip()
                    a4=a4.get().strip().upper()
                    a6=a6.get().strip().upper()
                    a7=a7.get().strip().upper()
                    a8=a8.get().strip().upper()
                    y=conv2(a5,a12)
                    x=a13
                    z=search1(a6,a7)
                    if z==0:
                        txt='\nSTATION NOT FOUND! TRY AGAIN OR SEE HELP'
                    elif z==-1:
                        txt='\nNO TRAIN FOUND BETWEEN THE STATIONS'
                    if z==0 or z==-1:
                        lb=Label(tkt,text=txt)
                        lb.pack()
                        return
                    if a8==''or a8 not in ['1A','2A','3A','SL']:
                        lb=Label(tkt,text='\n INVALID CLASS ENTRY!!!')
                        lb.pack()
                        return
                    else:
                        clas=['1A','2A','3A','SL']
                        p=[0,0,0,0]
                        dt=a9+'-'+a10+'-'+a11
                        for i in range(len(clas)):
                            if clas[i]==a8:
                                p[i]=int(a2)
                                ind=i
                            else:
                                p[i]=0
                        print(ind)
            
                        if x[0][ind]>=p[ind]:
                            import random
                            x[0][ind]=x[0][ind]-p[ind]
                            x[1][ind]=x[1][ind]+p[ind]
                            dic=dict(zip(clas,x[1]))
        
                            while True:
                                pnr=random.randint(1000000000,9999999999)
                                f=open(r'D:\projects\railway\PNRS\PNRS.txt','r')
                                if str(pnr) not in f.read():
                                    f.close()
                                    f=open(r'D:\projects\railway\PNRS\PNRS.txt','a')
                                    f.writelines('\n'+str(pnr))
                                    f.flush()
                                    break
                            fin=open(r'D:\projects\railway\PASSENGER\PASSENGER.txt','a')
                            txt=str(pnr)+','+a1+','+a2+','+a3+','+a4+','+a5+','+a6+','+a7+','
                            txt=txt+a8+','+a9+'-'+a10+'-'+a11+'\n'
                            fin.write(txt)
                            fin.close()
                            pth=r'D:\projects\railway\TRAINS\%s.txt'%y
                            fin=open(pth,'r+')
                            f2=open(r'D:\projects\railway\TRAINS\temp.txt','w')
                            i=fin.readline()
                            ctr=0
                            while i:
            
                                if dt in i:
                                    tct='('+"'"+dt+"',1A/"+str(dic['1A'])+",2A/"+str(dic['2A'])
                                    tct=tct+",3A/"+str(dic['3A'])+',SL/'+str(dic['SL'])+')\n'
                                    f2.write(tct)
                                    ctr=1
                                else:
                                    f2.write(i)
                                i=fin.readline()
                            if ctr==0:
                                tct='('+"'"+dt+"',1A/"+str(dic['1A'])+",2A/"+str(dic['2A'])
                                tct=tct+",3A/"+str(dic['3A'])+',SL/'+str(dic['SL'])+')'
                                f2.write('\n'+tct)
                            import os
                            fin.close()
                            f2.close()
                            os.remove(pth)
                            os.rename(r'D:\projects\railway\TRAINS\temp.txt',pth)
                            txt='\nBOOKING SUCCESSFUL\n\nHERE ARE THE BOOKING DETAILS:\n'
                            txt=txt+'PASSENGER\'S NAME: '+a1
                            txt=txt+'\nPNR NO: '+str(pnr)
                            txt=txt+'\n\nFOR DETAILS CHECK PNR ENQUIRY\n\nHAVE A SAFE JOURNEY :)'
                            
                            t=Text(tkt)
                            t.insert(INSERT,txt)
                            t.pack()
                            return
        
                        else:
                            txt= '\nREQUIRED SEATS NOT AVAILABLE'
                            lb=Label(tkt,text=txt,bg="#A7BEAE")
                            lb.pack()
                            return
                        
                def conv2(a1,a2):
                    fin=open(r'D:\projects\railway\TRAIN CODE\TRAIN CODE.txt','r')
                    abc=fin.read()
                    fin.seek(0)
                    i=fin.readline()
                    while i:
                        i=i.strip('\n()')
                        l=i.split(',')
                        if a1 == l[0] or a2 ==l[1]:
                            code=l[0]
                            return code
                        else:
                            i=fin.readline()
                def search1(a1,a2):
                    fin=open(r'D:\projects\railway\STATION CODE\STATION CODE.txt','r')
                    abc=fin.read()
                    if a1 in abc and a2 in abc and a1!='' and a2!='':
                        fin.seek(0)
                        i=fin.readline()
                        counter=0
                        while i:
                            i=i.strip('\n()')
                            l=i.split(',')
                            if (a1==l[0] or a1==l[1]):
                                if a1==l[1]:
                                    a1=l[0]
                                counter+=1
                            if (a2==l[0] or a2==l[1]):
                                if a2==l[1]:
                                    a2=l[0]
                                counter+=1
                            if counter==2:
                                break
                            else:
                                i=fin.readline()
                        else:
                            return 0
                        search2(a1,a2)
                    else:
                        return 0
                def search2(a1,a2):
                    TR=[10103,12553,12565,16176]
                    p=[]
                    for m in TR:
                        path=r'D:\projects\railway\TRAINS\%s.txt'%str(m)
                        fout=open(path,'r')
                        abc=fout.read()
                        if a1 in abc and a2 in abc:
                            fout.seek(0)
                            y=fout.readline();y=y.strip('\n')
                            z=fout.readline();z=z.strip('\n')
                            fout.seek(0)
                            c=fout.readlines()
                            for s in range(len(c)):
                                if c[s]=='STATIONS\n':
                                    begin=s+1
                                elif c[s]=='SEATS\n':
                                    end=s
                            rslt=c[begin:end]
                            for q in rslt:
                                a=q.strip('\n()')
                                a=a.split(',')
                                if a1==a[1].strip("'"):
                                    s1=int(a[0])
                                if a2==a[1].strip("'"):
                                    s2=int(a[0])
                
                            if s1-s2<0:
                                p.append([y,z])
                    if p==[]:
                        return -1
                    else:
                        return 1

                
        ##----------SECONDARY FRAME 5-----------
        def FRMH():
            frm1.destroy()
            global frmH
            frmH=Frame(root,bg="#A7BEAE")
            frmH.pack()

            #----------LABEL BUTTONS AND ENTRIES----------
            back_button(frmH)
            lb=Label(frmH,text='\n\n\n\n\n',bg="#A7BEAE")
            lb.pack()
            bt1=Button(frmH,text='Get Train Codes',bg='#E59866',fg='white',height=3,width=25,command=lambda:trcode())
            bt1.pack()
            bt2=Button(frmH,text='Get Station Codes',bg='#E59866',fg='white',height=3,width=25,command=lambda:stcode())
            bt2.pack()

            #----------TRAIN CODE FUNCTION------------
            def trcode():
                fin=open(r'D:\projects\railway\TRAIN CODE\TRAIN CODE.txt','r')
                i=fin.readline()
                txt='\nTHESE CODES ARE USED IN THE PROGRAM:\n\nTRAIN NO\t\tTRAIN NAME'
                while i:
                    a=i.strip('\n()').split(',')
                    txt=txt+'\n'+a[0]+'\t\t'+a[1]
                    i=fin.readline()
                frmH.destroy()
                FRMH()
                t=Text(frmH)
                t.insert(INSERT,txt)
                t.pack()

            #----------STATION CODE FUNCTION------------
            def stcode():
                fin=open(r'D:\projects\railway\STATION CODE\STATION CODE.txt','r')
                i=fin.readline()
                txt='\nTHESE CODES ARE USED IN THE PROGRAM:\n\nSTATION CODE\t\tSTATION NAME'
                while i:
                    a=i.strip('\n()').split(',')
                    txt=txt+'\n'+a[0]+'\t\t'+a[1]
                    i=fin.readline()
                frmH.destroy()
                FRMH()
                t=Text(frmH)
                t.insert(INSERT,txt)
                t.pack()
                    

    #------BACK BUTTON-------------
            
    def back_button(master,slave=None):

        def back():
            master.destroy()
            if slave:
                slave.destroy()
            FRM1()
            
        btn=Button(master,text='BACK',bg='#E59866',fg='white',height=1,width=7,command=lambda:back())
        btn.pack()

    #------TO CONVERT STATION CODE TO STATION NAME--------
    def conv(a1):
        fin=open(r'D:\projects\railway\STATION CODE\STATION CODE.txt','r')
        fin.seek(0)
        i=fin.readline()
        while i:
            i=i.strip('\n()')
            l=i.split(',')
            if a1==l[0]:
                a1=l[1]
                return a1
            else:
                i=fin.readline()

    #-------TO CONVERT TRAIN CODE TO TRAIN NAME----------
    def conv1(a1):
        fin=open(r'D:\projects\railway\TRAIN CODE\TRAIN CODE.txt','r')
        fin.seek(0)
        i=fin.readline()
        while i:
            i=i.strip('\n()')
            l=i.split(',')
            if a1==l[0]:
                a1=l[1]
                return a1
            else:
                i=fin.readline()
        
    FRM1()
    root.mainloop()


#---------WELCOME SCREEN CODE-----------

w1=Tk()
w1.overrideredirect(1)
user32=ctypes.windll.user32
sz_x=user32.GetSystemMetrics(0)
sz_y=user32.GetSystemMetrics(1)
w1_x=500
w1_y=272
ad_x=int((sz_x-w1_x)/2)
ad_y=int((sz_y-w1_y)/2)
size=str(w1_x)+'x'+str(w1_y)+'+'+str(ad_x)+'+'+str(ad_y)
w1.geometry(size)
ph=ImageTk.PhotoImage(Image.open(r'D:\projects\railway\PHOTOS\welcome.png'))
l1=Label(w1,image=ph)
l1.pack()
w1.after(5000, lambda:w1.destroy())
w1.mainloop()

#--------PASSWORD FRAME------------------
pwd=Tk()
pwd.title('Log IN')
pwd.configure(background="#E7E8D1")
pw=Frame(pwd)

#--------GEOMETRY OF PASSWORD FRAME---------
user32=ctypes.windll.user32
sz_x=user32.GetSystemMetrics(0)
sz_y=user32.GetSystemMetrics(1)
pwd_x=210
pwd_y=170
ad_x=int((sz_x-pwd_x)/2)
ad_y=int((sz_y-pwd_y)/2)
size=str(pwd_x)+'x'+str(pwd_y)+'+'+str(ad_x)+'+'+str(ad_y)
pwd.geometry(size)


def pw_frame():
    global pw
    pw=Frame(pwd,bg="#A7BEAE")
    pw.pack()
    un=Label(pw,text='Username',bg="#A7BEAE")
    un.pack()
    une=Entry(pw)
    une.pack()
    p=Label(pw,text='Password',bg="#A7BEAE")
    p.pack()
    pe=Entry(pw,show='*')
    pe.pack()
    bl=Label(pw,bg="#A7BEAE")
    bl.pack()
    btn=Button(pw,text='LOG IN',bg='#E59866',fg='white',command=lambda a1=une,a2=pe:check(a1,a2))
    btn.pack()
def check(a1,a2):
    fin=open(r'D:\projects\railway\PASSWORD\PASSWORD.txt')
    a1=a1.get()
    a2=a2.get()
    a=fin.readline().strip('\n')
    b=fin.readline()
    if a==a1 and b==a2:
        main()
    else:
        if a!=a1:
            txt='\nWRONG Username!'
        elif a!=a2:
            txt= '\nWRONG Password!'
        pw.destroy()
        pw_frame()
        lbl=Label(pw,text=txt,bg="#A7BEAE")
        lbl.pack()




#-------MAIN-------
pw_frame()
pwd.mainloop()