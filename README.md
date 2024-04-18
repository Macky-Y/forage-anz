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
<img width="540" alt="image" src="https://github.com/Macky-Y/forage-anz/assets/63437122/26a8aa79-0ab2-4921-9ac4-29707fff855d">
<br>
Sub-task 1: 

- anz-logo.jpg and bank-card.jpg are two images that show up in the users network traffic.
- Extract these images from the pcap file and attach them to your report.

To look at the images the user accessed named anz-logo.jpg and bank-card.jpg, I right-clicked on them and followed the TCP stream. The raw data string is too long, so I created a simple script that will automate the process of getting the raw data between the first hex (FFD8) and the last hex (FFD9), my script then will output it in a text file. This is the script I used:
<br>
<img width="356" alt="image" src="https://github.com/Macky-Y/forage-anz/assets/63437122/2b8f0d48-cb57-457e-a6bb-1909939721d3">
<br>
You can also download this script and the file name is script.py.
<br>
<br>
This is how the program works:
<br>
<img width="540" alt="image" src="https://github.com/Macky-Y/forage-anz/assets/63437122/998519ce-e0c1-4ada-9b72-31d18d5e67af">
<br>
<br>
And voila here is the extracted hex data:
<br>
<img width="245" alt="image" src="https://github.com/Macky-Y/forage-anz/assets/63437122/04d59143-5aff-47af-8764-6419dae9ee58">


</p>
