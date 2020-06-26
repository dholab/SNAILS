# SNAILS v1.0
Slow Nucleic Acid Instrument for Long Sequences

SNAILS is a 3D printed liquid handling robot. Its purpose is to improve ultralong genomic reads by reducing shearing due to pipetting. 

# Abstract
Background: Third-generation sequencing instruments such as Oxford Nanopore Technologies’ MinION are capable of producing ultra-long reads exceeding one million continuous base pairs. These technologies are becoming increasingly popular due to the advantages ultra-long sequencing data provides for de novo assembly of complex regions of the genome. Despite increasing popularity, little advancement has been made in preparing DNA for ultra-long sequencing. 

Results: Here we introduce SNAILS (small nucleic acid instrument for long sequences): a low-cost, 3D-printed pipette attachment that automates slow pipetting of reagents during ultra-long Oxford nanopore library preparation.  By minimizing shearing of DNA during library preparation, SNAILS out-performing manual preparation in preservation of reads exceeding one million base pairs. 

Conclusions: SNAILS is the first improvement to ultra-long read retention through the process of library preparation. 

<img src="/readme_images/F1_V2b_PNG.png" alt="F1_V2b_PNG" width="750"/>

# Printing Instructions
We used Ultimaker 3, S3, and S5 3D printers with the Ultimaker Cura program (https://ultimaker.com/software/ultimaker-cura). We recommend PLA for the printing material with the point set to 0.2 mm and infill at 20% for all the pieces. For the base, motor holder, and bridge, support material needs to be included, and changing the support density to 25 for a smoother print job is recommended. Additionally, we recommend that the base is printed on a separate build plate than the other pieces because it is so much thinner and by separating the pieces you increase the chances of a successful print job. More detailed, step-by-step printing instructions are directly below.

## Instructions for 3D printing SNAIL robot using an Ultimaker Cura
1. Connect to printer – this must be the first step because any and all settings altered will change anytime the printer is changed. You can connect to the printer through an IP address or network connection; follow the instructions on the screen. I used an Ultimaker 3 for the base and an Ultimaker S5 for the other four pieces; however, you can use any combination to print all the pieces. If you use a printer smaller than an S5 make sure it can still fit the towers and do not print all four pieces together. When printing multiple pieces at once, make sure the heights are about equal and the plate isn’t too full (Fig. 4 is the most crowded a plate should be). The base should be printed separate the other pieces because it is so much thinner than the others to increase the chances of a successful print. Once the printer is selected your screen should look like this:
<img src="/readme_images/1.png" alt="1" width="500"/>
2. Open a file folder with all the STL files and drag those files into Cura onto the schematic of the printer.
3. Click on the part(s) and use the toolbar along the left side to rotate and move the parts (the next two pictures depict these movements) so that it lies flat on the printer and reduces support material. The pieces should be oriented as depicted below to produce the best prints.
<img src="/readme_images/3a.png" alt="3a" width="500"/>
<img src="/readme_images/3b.png" alt="3b" width="500"/>
<img src="/readme_images/3c.png" alt="3c" width="500"/>
4. Set the material types to PLA and make sure it is communicating with the printer. If the material changes later, all settings will go back to the defaults.
<img src="/readme_images/4.png" alt="4" width="500"/>
5. Go to Print Settings in the upper right. 
    - Layer Height: 0.2 (use 0.1 for the base)
    - Infill %: 20
    - Support: Check, Extruder 1 (if you only have one material in the printer this option will disappear, but if there are multiple materials make sure you choose the correct extruder)
    - Adhesion: Check
    - Custom -> Support -> Support Density: 25 (this setting isn’t crucial to change if it isn’t available on your machine, but it will make upper edges smoother)
<img src="/readme_images/5.png" alt="5" width="500"/>
6. Click the blue Slice in the bottom right.
7. Click Preview at the top middle to verify the correct material and support material are produced. There is a scroll along the right side to view each layer. Change the color scheme to Line Type to more easily view the support.
<img src="/readme_images/7.png" alt="7" width="500"/>
8. If everything looks correct, verify the printer is ready and click the blue, Print button in the bottom right. Make sure that the printer receives the print before leaving.

## Assembling
Once the 3D printing is complete, all of the support material must be removed and all of the pieces should be able to snap together. Due to the margin or error from an Ultimaker, it possible some of the pieces will need to be slightly shaved down with a dremel to fully remove the border support material. Regardless, the pieces intentionally are designed to fit tightly together to avoid moving while running so light taps from a mallet may help to make the joints fully flush.

# Circuitry
Raspbian v4.19 (https://www.raspberrypi.org/downloads/raspbian/) was installed using NOOBS v3.3.1 (https://www.raspberrypi.org/downloads/noobs/) to a 32 GB micro sd card and booted on a Raspberry Pi (rpi) model 3B+. Electronic components were assembled into a solderless circuit as depicted in Figure 1C. Briefly, the rpi GPIO pins 23,24, 25, and ground pin 6 were connected to IN1, IN2, ENA, and GND terminals of the L298N motor driver board (https://www.sunfounder.com/product-l298n-motor-driver-board-module.html), respectively. The positive and negative leads of a 12V DC power supply were connected to the 12V and GND terminals of the L298N motor driver, respectively. Finally, the two terminals of a 12V DC planetary motor ((https://www.servocity.com/12-rpm-hd-premium-planetary-gear-motor) were connected to the OUT1 and OUT2 terminals of the L298N motor driver.
<img src="/readme_images/circuit_PNG.png" alt="circuit_PNT" width="500"/>

# Results
<img src="/readme_images/Table1.png" alt="Table1" width="700"/><img src="/readme_images/Table2.png" alt="Table2" width="300"/>
