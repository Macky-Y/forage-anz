<p align="center">
  <img src="./anz/anz_logo.jpg">
</p>

<h1 align="center">Forage Virtual Experience Write-up - ANZ</h1>
<br>
<p>
<b>Technologies Used: </b>
  
- Wireshark
- Hex Editor (Hex Fiend for macOS, you can use HxD if you are using Windows)
- Visual Studio Code
- Python
<br>
Packet Capture Analysis:
<br>
Analyzing a packet capture from a network provided to me. I filtered it to HTTP traffic to look at the contents of the HTTP packet.
<br>
Note: You can also download the pcap file if you want to follow along.
<br>
<p align="center">
<img width="540" alt="image" src="https://github.com/Macky-Y/forage-anz/assets/63437122/26a8aa79-0ab2-4921-9ac4-29707fff855d">
</p>
<br>
Sub-task 1: 

- anz-logo.jpg and bank-card.jpg are two images that show up in the users network traffic.
- Extract these images from the pcap file and attach them to your report.

To look at the images the user accessed named anz-logo.jpg and bank-card.jpg, I right-clicked on them and followed the TCP stream. The raw data string is too long, so I created a simple script that will automate the process of getting the raw data between the first hex (FFD8) and the last hex (FFD9), my script then will output it in a text file. This is the script I used:
<br>
<p align="center">
<img width="356" alt="image" src="https://github.com/Macky-Y/forage-anz/assets/63437122/2b8f0d48-cb57-457e-a6bb-1909939721d3">
<br>
You can also download this script and the file name is script.py.
</p>
<br>
<br>
<p align="center">
This is how the program works:
<br>
<img width="540" alt="image" src="https://github.com/Macky-Y/forage-anz/assets/63437122/998519ce-e0c1-4ada-9b72-31d18d5e67af">
</p>
<br>
<br>
<p align="center">
And voila here is the extracted hex data:
<br>
<img width="245" alt="image" src="https://github.com/Macky-Y/forage-anz/assets/63437122/04d59143-5aff-47af-8764-6419dae9ee58">
</p>
<br>
<p align="center">
I copied and pasted it to my hex editor and saved it as JPG file format to view the data and this is what I found:
anz_logo.jpg
<br>
<br>
<img src="./anz/anz_logo.jpg">
<br>
bank-card.jpg
<br>
<img src="./anz/bank-card.jpg">
</p>
<br>
Sub-task 2: 

- The network traffic for the images "ANZ1.jpg" and "ANZ2.jpg" is more than it appears.
- Extract the images, include them and mention what is different about them in your report.
<p align="center">
The same method applies when extracting images, after performing the previous steps, these are the images I found:
<br>
<br>
ANZ1.jpg
<br>
<img src="./anz/anz1.jpg" width="540">
<br>
<br>
ANZ2.jpg
<br>
<img src="./anz/anz2.jpg" width="540">
<br>
<br>
I saw this message at the end of the hex data of these images:
</p>
<p align="center">
For anz1.jpg:
<br>
<img width="540" alt="image" src="https://github.com/Macky-Y/forage-anz/assets/63437122/748c8a59-8007-4872-babe-8a6747ffac1b">
<br>
<br>
For anz2.jpg:
<br>
<img width="430" alt="image" src="https://github.com/Macky-Y/forage-anz/assets/63437122/af2c3c6c-b7cb-4e88-8937-9b4f03ebbcc0">
</p>
Sub-task 3: 

- The user downloaded a suspicious document called "how-to-commit-crimes.docx"
- Find the contents of this file and include it in your report.

<p align="center">
I checked this specific traffic and found this:
<br>
<img width="261" alt="image" src="https://github.com/Macky-Y/forage-anz/assets/63437122/5ade7647-197c-4c9c-90da-f141360cc1ea">
</p>
<br>
Sub-task 4: 

- The user accessed 3 pdf documents: ANZ_Document.pdf, ANZ_Document2.pdf, evil.pdf
- Extract and view these documents. Include images of them in your report.
  
<p align="center">
This time I did it differently, I utilized the search function on wireshark and put the hex data on raw. I searched for “25504446” since it is a pdf file signature, I copied and pasted from 25504446 until the end of the hex data. I did it to all these pdf files and here are the results:
<br>
<br>
anz_doc1.pdf
<br>
<img width="181" alt="image" src="https://github.com/Macky-Y/forage-anz/assets/63437122/b400e0f2-c025-41e3-8bf3-52b450be2936">
<br>
<br>
anz_doc2.pdf
<br>
<img width="323" alt="image" src="https://github.com/Macky-Y/forage-anz/assets/63437122/cca65b11-d220-4c73-9e86-0a3a0bb00419">
<br>
<br>
evil.pdf
<br>
<img width="490" alt="image" src="https://github.com/Macky-Y/forage-anz/assets/63437122/228582ad-6441-49f7-9a91-64ec781efa09">
</p>

Sub-task 5: 

- The user also accessed a file called "hiddenmessage2.txt"
- What is the contents of this file? Include it in your report

<p align="center">
For this one, I can’t find the txt signature file, so I tried typing ffd8 and it worked, I believe this is a jpg file hidden in a txt file, I found this image:
<br>
<br>
hiddenmessage.jpg
<img src="./anz/hiddenmessage.jpg">
</p>
<br>
Sub-task 6: 

- The user accessed an image called "atm-image.jpg"
- Identify what is different about this traffic and include everything in your report.
<p align="center">
I noticed there are 2 FFD8 in the hex value, leaving me puzzled, so I tried breaking it into 2 and yes I found 2 photos. Here are the photos I gathered:
<br>
<br>
atm.jpg
<br>
<img src="./anz/atm.jpg">
<br>
<br>
atm2.jpg
<br>
<img src="./anz/atm2.jpg">
</p>

Sub-task 7: 

- The network traffic shows that the user accessed the image "broken.png"
- Extract and include the image in your report.

<p align="center">
I’ll be honest but this is the section I kind of struggled with, so I pasted the ASCII data to chatgpt and was informed that this is a base64 encoding. I looked online for a base64 conversion tool and the result I have is this image:
<br>
<br>
<img width="201" alt="image" src="https://github.com/Macky-Y/forage-anz/assets/63437122/cbf012ca-541b-4d5a-a665-1c56a37166d7">
</p>

Sub-task 8: 

- The user accessed one more document called securepdf.pdf
- Access this document include an image of the pdf in your report. Detail the steps to access it

<b> These are the steps I took for this task:</b>
<br>

1. I tried looking at the packet and it is not a pdf file since it is not finding the pdf signature, so again I posted this hex value to chatgpt and I was told that this was a zip file.
2. I looked for online tool that can convert this hex to zip file.
3.  After I did that, the zip file was reconstructed, but I was asked for a password.
4.  I looked at the ASCII data of the packet and looked at the very bottom and found this: <br>
<p align="center">
<img width="397" alt="image" src="https://github.com/Macky-Y/forage-anz/assets/63437122/dea51a3c-33b4-4a58-a939-08e4a9d8a4ac">
</p>
<br>
<br>
Lastly, I went back to the file and put “secure” as the password and yes it gave me a pdf file called rawpdf.pdf. I opened it and I was presented with 2 pages of pdf. Here is the image:
<br>
<p align="center">
<img width="402" alt="image" src="https://github.com/Macky-Y/forage-anz/assets/63437122/3d10ea8d-6e82-41b1-8f63-e85f932fe449">
</p>
</p>

<br>
<br>
<br>
<br>
<p align="center"> 
  I hope you found value in this write-up. Thank you for dedicating your time to reading it and joining me on my cybersecurity journey!
</p>
