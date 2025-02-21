This document is intended to be a living document about the processes for labeling for the FishSense project.

# Getting Started
Please log in to [Labeler](https://labeler.e4e.ucsd.edu).  If you do not yet have an account, please contact your team lead or a Label Studio admin to access the system.

After logging in, you will have a page listing all available labeling projects.  Please only label for projects that you have been asked to label.  Each project may have specific instructions for what they need to be labeled.  The instructions for FishSense are described in the sections below.  This section will discuss general Label Studio usage.

After opening a project, please click the blue "Label All Tasks" button.  This will provide you with the best labeling experience.

To label, follow these steps:
1. If there is nothing to label, simply click submit.  Otherwise, follow the remaining steps.
2. Zoom into the image as necessary.  Use the zoom/pan controls to the right of the image.
3. Select the appropriate label for your image.
4. Select the point or points you wish to label.  Your labels appear on the screen and in the bottom right of your display.
5. When finished, click submit.

# Lasers
Navigate to the [FishSense Laser](https://labeler.e4e.ucsd.edu/projects/10) in Label Studio.

You will be presented with images containing zero, one, or two lasers.  The majority of these images will contain only a single laser.  These lasers may be red or green.  So that this data can be used for both processing and data analysis, please select the proper label for the laser you are labeling.  For example, if you are labeling a red laser, please select "Red Laser" as your label.  It is necessary to get the dot as close to the center of the laser as possible.  Error in distance measurements are introduced if not properly centered.


# Grouper Moon
**Step 1:** Make sure you already have an account on label studio. If not, refer back to "getting started" section.\
**Step 2:** log in and select the Grouper Moon project. 
<img width="781" alt="Screenshot 2024-11-27 at 1 31 32 PM" src="https://github.com/user-attachments/assets/f7aa89e5-1ce7-479e-a22b-1e3d3219d25e">

**Step 3:** Select "Label All Tasks."
<img width="769" alt="Screenshot 2024-11-27 at 1 44 58 PM" src="https://github.com/user-attachments/assets/9d241099-d527-42f6-b914-1183746ee6b8">

**Step 4:** Turn on "Auto-Annotation."
<img width="996" alt="Screenshot 2024-11-27 at 4 44 22 PM" src="https://github.com/user-attachments/assets/89b3d9ac-610a-43fb-b067-bfff1100a444">

**Step 5:** Start segmentation labeling.\
There are three ways of labeling-- using brush, keypoint, or rectangle. 
- **Brush Labels**\
    Choose brush. Then click "Fish 1" under "Brush Labels."

<img width="988" alt="Screenshot 2024-12-07 at 5 09 30 PM" src="https://github.com/user-attachments/assets/1918125c-7c48-437c-ac82-f1d05a15b086">

Now you're able to manually draw segmentation mask for fish! 

- **Keypoint Labels (recommended)**\
    Click on "Auto-Detect" and choose keypoints. Then choose "Fish 3" under "Keypoint Labels."

<img width="982" alt="Screenshot 2024-11-27 at 5 04 11 PM" src="https://github.com/user-attachments/assets/d7098308-4cf2-4d59-a46e-0fd8a31fb352">
   
- Place key points on the target fish(you can only put one key point at a time). A mask will be generated based on the key point.
- If the mask looks good to you, accept it. If you need to make adjustments to the mask, select the mask and then use brush or eraser to do manual adjustment.
- Also remember to delete the key point labels afterwards.(We only need the segmentation labels!)
 
<img width="1000" alt="Screenshot 2024-11-27 at 5 14 10 PM" src="https://github.com/user-attachments/assets/d7f5f418-ab14-4a24-9b31-794800b7fe33">

- **Rectangle Labels (recommended)**\
     Click on "Auto-Detect" and choose rectangle. Then choose "Fish 5" under "Rectangle Labels."
<img width="1001" alt="Screenshot 2024-11-29 at 7 00 54 PM" src="https://github.com/user-attachments/assets/f10df5c4-7962-41f1-a04b-3048ba596c61">
    
- Draw a bounding box around the target fish. A mask will be generated automatically based on the bounding box.
- If the mask looks good to you, accept it. If you need to make adjustments to the mask, select the mask and then use brush or eraser to do manual adjustment.
- Also remember to delete the bounding box labels afterwards.(We only need the segmentation labels!)

**Criteria for labeling(important!)**:
- Please label all the fish you can see. You can skip the fish that are too blurry in the image.


**Special Cases**: 
- Please label separate regions for individual fish. For example, if two fish overlap, we want two separate labels instead of only one label for both fish. 
 