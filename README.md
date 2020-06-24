# SNAILS v1.0
Slow Nucleic Acid Instrument for Long Sequences

SNAILS is a 3D printed liquid handling robot. The STL files in this folder include all of the parts required to build the body of the robot. A raspberry pi, motor driver, motor, and standup pipette are also required for the full assembly as described in our paper.

# Printing Instructions
We used Ultimaker 3, S3, and S5 3D printers with the Ultimaker Cura program (https://ultimaker.com/software/ultimaker-cura). We recommend PLA for the printing material with the point set to 0.2 mm and infill at 20% for all the pieces. For the base, motor holder, and bridge, support material needs to be included, and changing the support density to 25 for a smoother print job is recommended. Additionally, we recommend that the base is printed on a separate build plate than the other pieces because it is so much thinner and by separating the pieces you increase the chances of a successful print job. More detailed, step-by-step printing instructions are directly below.

## Instructions for 3D printing SNAIL robot using an Ultimaker Cura
1. Connect to printer – this must be the first step because any and all settings altered will change anytime the printer is changed. You can connect to the printer through an IP address or network connection; follow the instructions on the screen. I used an Ultimaker 3 for the base and an Ultimaker S5 for the other four pieces; however, you can use any combination to print all the pieces. If you use a printer smaller than an S5 make sure it can still fit the towers and do not print all four pieces together. When printing multiple pieces at once, make sure the heights are about equal and the plate isn’t too full (Fig. 4 is the most crowded a plate should be). The base should be printed separate the other pieces because it is so much thinner than the others to increase the chances of a successful print. Once the printer is selected your screen should look like this:
![](/readme_images/1.png)
2. Open a file folder with all the STL files and drag those files into Cura onto the schematic of the printer.
3. Click on the part(s) and use the toolbar along the left side to rotate and move the parts (the next two pictures depict these movements) so that it lies flat on the printer and reduces support material. The pieces should be oriented as depicted below to produce the best prints.
![](/readme_images/3a.png)
![](/readme_images/3b.png)
![](/readme_images/3c.png)
4. Set the material types to PLA and make sure it is communicating with the printer. If the material changes later, all settings will go back to the defaults.
![](/readme_images/4.png)
5. Go to Print Settings in the upper right. 
    - Layer Height: 0.2 (use 0.1 for the base)
    - Infill %: 20
    - Support: Check, Extruder 1 (if you only have one material in the printer this option will disappear, but if there are multiple materials make sure you choose the correct extruder)
    - Adhesion: Check
    - Custom -> Support -> Support Density: 25 (this setting isn’t crucial to change if it isn’t available on your machine, but it will make upper edges smoother)
![](/readme_images/5.png)
6. Click the blue Slice in the bottom right.
7. Click Preview at the top middle to verify the correct material and support material are produced. There is a scroll along the right side to view each layer. Change the color scheme to Line Type to more easily view the support.
![](/readme_images/7.png)
8. If everything looks correct, verify the printer is ready and click the blue, Print button in the bottom right. Make sure that the printer receives the print before leaving.

## Assembling
Once the 3D printing is complete, all of the support material must be removed and all of the pieces should be able to snap together. Due to the margin or error from an Ultimaker, it possible some of the pieces will need to be slightly shaved down with a dremel to fully remove the border support material. Regardless, the pieces intentionally are designed to fit tightly together to avoid moving while running so light taps from a mallet may help to make the joints fully flush.
![](/readme_images/F1_V2b_PNG.png)
