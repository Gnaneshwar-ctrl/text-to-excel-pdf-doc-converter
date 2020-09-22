import cv2
from fpdf import FPDF
import docx 
import pandas as pd
import numpy as np
c = int(input("want .xlsx choose 1 or .pdf choose 2 or .doc choose 3 ::"))
if(c == 1):
    df = pd.read_csv("Test!.txt",sep = ':') 
    df.to_excel("/Users/gnane/Desktop/output.xlsx", 'Sheet1')
    
if(c == 2):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times",size = 10)
    fd = open("Test!.txt","r")
    
    for i in fd:
        if(i != ":"):
            pdf.cell (200, 10, txt = i, ln = 1, align = 'C')
        else:
            pdf.cell (200, 10, txt = "        ", ln = 1, align = 'C')
    pdf.output("/Users/gnane/Desktop/output.pdf")
        
