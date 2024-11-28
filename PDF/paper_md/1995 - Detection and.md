# Detection and Counting of Uneaten Food Pellets in a Sea Cage Using Image Analysis

**M. Foster**  
MPR Teltech Ltd, 8999 Nelson Way, Burnaby, BC, Canada V5A 4B5

**R. Petrell\***  
Bio-Resource Engineering, 2357 Main Hall, University of British Columbia, Vancouver, BC, Canada V6T 1Z4

&

**M. R. Ito & R. Ward**  
Electrical Engineering, University of British Columbia, Vancouver, BC, Canada V6T 1W5

*(Received 12 June 1993; accepted 8 August 1994)*

## ABSTRACT

The purpose of this study was to detect and count feed pellets in a sea cage using underwater video cameras. Using a light-compensating camera pointing straight down in the water column, extruded pellets appear white. This effect made it possible to detect and count feed pellets during a feeding event. **The manual counting of food pellets from video replay is laborious so algorithms were developed for detection and counting of food pellets from recorded video image sequences.** The algorithms were implemented on a personal computer based image processing system. Experiments were performed to test the algorithms with pellet densities used in actual feeding situations. The average count error was approximately ± 10%. By increasing the video sampling rate and screening off the cameras from the fish, this error could be significantly reduced.

---

*Mention of trade names in this publication is solely for the purpose of providing specific information and does not constitute endorsement over others of a similar nature not mentioned.*  
***To whom all correspondence should be addressed.***




## INTRODUCTION

Reducing feed wastage on salmon sea cage farms would affect fish farm operating costs, profits, appropriate additive delivery and the magnitude of the environmental impact. Salmon feed represents 45-60% of the operating costs on a commercial-sized sea cage farm (British Columbia Salmon Farmers Association, 1993). **The feed conversion ratio, FCR, is used as a measure of feed usage and is defined as the ratio of the feed distributed to the mass gain of the fish.** The industry average FCR is 1·5 for Atlantic salmon and 2·0 for chinook salmon (British Columbia Salmon Farmers Association, 1993). **The rations used to calculate those values included uneaten feed pellets because the farmers do not measure or control pellet loss.** Feed losses have been reported to range between 15 and 40% on commercial-sized sea cage farms (Seymour & Bergheim, 1991; Thorpe *et al.*, 1990). Under more controlled farming conditions, a FCR of 1·0 was achieved for Atlantic salmon without negatively affecting growth (Austreng *et al.*, 1987; Storebakken & Austreng, 1987). The optimal FCR would be the one which produces the largest fish using the least amount of feed. To determine the optimal FCR, feed wastage should be quantified.

Salmon are fed by hand for 4 h/day in the winter months, and 8 h/day in the summer months. **Large feed pellet losses adversely affect the environment, fish health and fish quality.** Uneaten pellets accumulate underneath sea cages and attract wild fish. Knowing the rate of accumulation can help farmers decide on production scheduling and feeding strategies. Knowledge of pellet loss is critical for assuring proper dose delivery when the pellets contain coloring agents, vaccines, vitamins or antibiotics.

**To accurately measure the ration and feed wastage, fish farmers need a measurement tool to give them feedback on pellet loss during a feeding period.** Aquaculture researchers would also benefit if a system were available to provide data on how much feed is not being eaten when they run feeding experiments. **Hydroacoustic detection of food pellets** (Juell, 1991; Juell *et al.*, 1993) is one method used to detect food waste. A hydroacoustic sensor is used to detect food waste (a group of uneaten food pellets) and signal an automatic feeder (The AquaSmart, Tasmania Technopark Centre). The automatic feeder is turned off when food waste is detected. The system does not count the uneaten food pellets, and therefore cannot be used for more complex automatic feeder control. **Another method of estimating food waste is to suspend a tarpaulin below the sea cage during the feeding period** (Shepherd & Bromage, 1988), retrieve it after feeding, and count the food pellets. This method does not provide immediate feedback during feeding. Only after feeding does the


can the wastage be assessed. **A new development is using a pump to return uneaten pellets from the cage bottom to the surface (Moore Clark Ltd, Vancouver, BC). Installation and equipment costs are high.**

The objectives of this study were to determine the applicability of a manual video camera based pellet detection and counting system, and to develop an automatic version of this manual system using image analysis algorithms. A farmer would be able to lower a video camera (pointing straight down) to a desired depth, and using video replay, count the number of pellets that are falling through the view area of the camera (Fig. 1) at that depth. **The view area is the base of a right square pyramid with height equal to the maximum depth from the camera that a pellet can be detected.** With this information, the farmer would have some numerical data on how much feed is being eaten by the fish above camera level. By placing the camera near the bottom of the sea cage, an estimate of how much feed is being wasted would be obtained. This system could be used to record the change in pellet loss during a feed event, as well as calculate the total amount lost.

The manual approach to counting food pellets from video replay could be laborious depending on the length of the feeding period. An operator would have to watch a videotape of the entire feeding period and keep an accurate count of the food pellets falling past the camera. **An automatic pellet counting algorithm using recorded image sequences was therefore developed and tested.**

There were two major steps involved in the development of the automatic counting system. These were, detecting the food pellets in the images, and correctly tracking food pellets from one image to the next. A typical image from the underwater camera would contain food pellets and salmon. The salmon are dark in color when viewed from above, but

![Video Camera](2_0.png)

**Fig. 1.** View area of video camera.


parts of the fish's body can appear white if the salmon turns on its side. Occasionally, other objects which appear light in color are present in the water. It was important to distinguish salmon and other objects from food pellets so they were not included in the food pellet count. Tracking objects was necessary to ensure each pellet was only counted once.

The automatic algorithms developed were used to: (1) isolate the pellet and non-pellet objects in the image; (2) measure features of the objects and classify them as food pellets or other objects; (3) track pellets from one frame to another; and (4) maintain a count of the number of pellets that have passed through the view area of the underwater camera (Fig. 2).

## MATERIALS AND METHODS

The image acquisition equipment consists of a Panasonic WV-B400 black and white CCD (Charge Coupled Device) camera with underwater housing and external controls (approximately US $2848), and a JVC AG-1960 super VHS (400 lines of resolution) videotape recorder (Fig. 3). The camera aperture is automatically controlled, and compensates for the illumination level.

![](3_0.png)

**Fig. 2.** Pellet counting process.


Detection and counting of feed pellets in a sea cage

![Image](4_0.png)

Sea Cage  
15m x 15m x 21m deep

Fig. 3. Video camera, rig, and video equipment used for image sequence acquisition.

The image analysis equipment consists of: an IBM compatible PC, dual displays (computer monitor and image monitor), an Imaging Technologies frame grabber (ITX-OFG), and a JVC BR-S822U super VHS videotape recorder (Fig. 4). The videotape recorder is equipped with a time code generator-reader expansion card, a time base correction card, and a RS-232 interface port. The recorder is used to extract sequences of images from super VHS videotape. The machine is capable of laying time codes on one of the audio tracks of a videotape. The time codes are used to identify each individual frame on the videotape. The computer can be used to search for a specific frame on the videotape by reading the time codes on the tape. When the desired frame has been reached, it can be acquired by the frame grabber card, and stored on the hard disk for later analysis. Using the time codes on the tape, a sequences of frames can be captured and stored automatically at a desired sampling rate. The videotape signal from the video recorder is digitized by the frame grabber. Each pixel is assigned a gray level in the range 0 (black) to 255 (white).


256

M. Foster, R. Petrell, M. R. Ito, R. Ward

![](5_0.png)

Fig. 4. Image analysis equipment.

Preprocessing of frame sequence

Food pellets are manufactured using an extrusion process and they are cylindrical in shape. The sides are very smooth, and the ends where the pellets were broken off after extrusion are rough. Food pellets were measured to be approximately 5-6% reflective. Although the food pellets appear dark brown to black on the surface, they appear white in images taken in the water with the underwater camera pointing downward. This effect is observed because the camera is highly sensitive (0.5 lux), and is designed to automatically compensate for the amount of light available. The camera opens the aperture in order to make the overall light level about 18% (where 0% is black and 100% is white).

To preprocess the frame sequence, the objects present in the image are separated from the background. This is accomplished by thresholding each image. Thresholding involves changing the value of each pixel in the image depending on whether its intensity value is above or below a chosen threshold value. If the pixel has an intensity value greater than the threshold value, it is set to 255 (white). If the pixel has an intensity value less than or equal to the threshold value, it is set to 0 (black). In this application, the food pellets are lighter in color than the background, so setting the threshold value just above the maximum gray level of the background separates the food pellets from the background. The back-


Detection and counting of feed pellets in a sea cage

ground gray level distribution resembles a normal distribution. The image is thresholded at the gray level 3 SDs from the estimated background mean gray level. After thresholding, the majority of pixels representing food pellets have values of 255, and the pixels in the rest of the image have values of 0. Thresholding is followed by dilation and erosion operations (Pratt, 1991) to fill in small areas of the objects, and remove extra pixels that are not part of objects.

### Object detection

After an image has been thresholded, there are many algorithms that can be used to detect the objects present in the image. In the current implementation, the binary (only two pixel values: 0 or 255) image is scanned row by row. If a pixel with a value of 255 is encountered, all the neighbors of that pixel with a value of 255 are determined. Then the neighbors of those pixels with a value of 255 are determined. This repetitive search continues until the edges of the object are reached. Pixels which form the object are marked so they are not used when scanning for additional objects. The centroid and area of the object are then calculated and stored, and the row by row scan is continued. When the scan reaches the end of the image, a list of the area and centroid of each object in the image has been stored.

Since the camera is viewing a three-dimensional medium, two or more food pellets can appear to overlap in the image. Overlapping objects must be separated before counting to ensure an accurate pellet count. To separate overlapping objects, the boundary of the object is determined, and an estimate of curvature is calculated for each pixel in the boundary. Figure 5 shows two objects with plots of their corresponding boundary curvatures. The first object is an object that should not be divided, while the second object is an object which should be divided.

The curvature around the boundary of the first object is fairly constant, while the curvature around the boundary of the second object becomes negative in two areas. These areas indicate how to separate the two overlapping objects (Poon *et al.*, 1992). Two boundary pixels, one from within each of the areas of negative curvature are joined together with a black line to divide the overlapping objects. This method works well for two overlapping objects, but does not work for three or more overlapping objects. It is assumed that three or more overlapping objects will not occur frequently.

In some cases, small negative curvature values are calculated for boundary points that do not correspond to points where the object should be divided. When there are more than two areas of negative


258

M. Foster, R. Petrell, M. R. Ito, R. Ward

![](7_0.png)

Fig. 5. Plots of curvature for two objects.

curvature, the two areas containing the largest negative curvatures are used for object separation. Large objects that should not be divided tend to have more areas of negative curvature than small objects. The reason that large objects are more likely to have areas of negative curvature is that as object size increases, the average curvature of the object decreases, and therefore small variations in curvature can result in areas of negative curvature. This does not occur for small objects. Since the average curvature is large for small objects, small variations from the average curvature will still be positive. In order to prevent division of large objects that should not be divided, the curvature values are adjusted before zero crossing detection is done. The amount of adjustment depends on the size of the object. If the object is small, the curvature values should not be changed a great deal. It is acceptable to subtract a small constant curvature from all the pixels in a small objects. This constant amount should not be large enough to cause objects to be divided that should not be divided. If the object is large, a constant curvature should be added to prevent objects that should not be divided from being divided. The constant amount should not be so large that large objects that should be divided are not divided.

The curvature values are adjusted as follows:

$$
\text{curvature}[i] = \text{curvature}[i] + \frac{K_1}{C_{AVG}} - K_2 \tag{1}
$$

where $C_{AVG}$ = average curvature of all boundary points with positive curvature, and $K_1$ and $K_2$ are constants


## 8_0.png

**Detection and counting of feed pellets in a sea cage**

For large objects, the average curvature will be small, so the second term should be large (larger than $K_2$), and a positive constant will be added. For small objects, the average curvature will be large, so the second term will be small (slightly smaller than $K_2$) and a small negative constant will be added.

### Object classification

After objects have been detected in the image, it must be determined which objects represent food pellets, and which objects represent fish and other particles or objects in the water. Properties (features) of the objects are measured, and these values are used to classify each object as either a food pellet or something else. In the classification process, an object is identified as being a member of one of a number of groups (or classes) based on its characteristics. Features of the object are measured in order to quantify the characteristics of the object. The measured characteristics can then be numerically compared to the classes and a decision regarding which class the object is a member of can be made. In this application, objects are classified as being a member of one of two groups: food pellet objects, or other objects.

Four features were used in this application. These features are invariant to rotation and scaling because food pellets can appear in different orientations, and at different distances from the camera. The four features were:

1. $$ \text{circularity} = \frac{{\text{perimeter}^2}}{{4 \pi \cdot \text{area}}} \quad (2) $$

2. $$ \text{bounding area ratio} = \frac{{\text{object area}}}{{\text{bounding box area}}} \quad (3) $$

The orientation of the bounding box was calculated using a method described by Pratt (1991):

3. $$ \text{minor to major axis ratio} = \frac{{\text{length of minor axis}}}{{\text{length of major axis}}} \quad (4) $$

4. $$ \text{minimum to maximum radius ratio} = \frac{{\text{minimum radius of object}}}{{\text{maximum radius of object}}} \quad (5) $$


260

To generate the classification function, these four feature values were calculated for 1686 objects (learning set) which were known to be food pellets. The class mean values for each feature, and the covariance matrix for the four features were calculated. Unknown objects can then be classified by calculating the distance from the measured feature values of the object to the class mean. The minimum intra-class distance (MICD) (Duda & Hart, 1973) is used which takes into account the correlation between features and the unequal variances of the features. The distance measure is:

$$
d_{MCID}(x, m) = [(x - m)^T S^{-1} (x - m)]^{0.5}
$$

where $x$ is the feature vector for the object to be classified, $m$ is the class mean feature vector, $S$ is the covariance matrix for the four features and $T$ indicates the transpose of a matrix.

Objects within a certain distance from the class mean are said to be members of the class. This distance can be adjusted depending on the classification requirements. In this application, the distance was determined by measuring the MICD distance for 312 objects representing food pellets, and the distance was chosen such that 97% of the pellets are detected.

### Object tracking and counting

Object tracking was implemented in order to track a single object throughout the sequence of frames so it is only counted once.

The geometry of pellet motion is shown in Fig. 6. It can be seen that when food pellets fall through the view area of the underwater camera, they will always enter the image frame at one of the edges. If a food pellet falls straight down the water column, the pellet motion in the image frame will be from the edge of the frame inward. These two properties were used to develop the object counting algorithm.

The counting algorithm uses two consecutive frames, Frame $i$ and Frame $i + 1$ which have both undergone object detection. Figure 7 shows Frame $i$ and Frame $i + 1$ with some food pellets and the New Object Area labeled.

The object counting algorithm involves tracking objects from Frame $i$ to Frame $i + 1$ and counting new objects in Frame $i + 1$ that have just entered the view area of the underwater camera. The new objects that are counted are objects that were not tracked from Frame $i$, and are located in a thin band around the edge of the frame (New Object Area). The count consists of objects that enter the view area of the camera and pass through the New Object Area. The algorithm is presented below.


# Detection and counting of feed pellets in a sea cage

![Food pellet motion](10_0.png)

**Fig. 6.** Food pellet motion.

---

**Fig. 7.** Two consecutive image frames.

---

## Object counting algorithm

1. Execute object matching algorithm between objects in Frame $i$ and Frame $i+1$.
2. All objects in the New Object Area of Frame $i+1$ that were not matched with objects in Frame $i$ are counted, and the resulting number is added to the total pellet count.
3. $i = i + 1$.
4. If frame $i + 1$ exists, GOTO Step 1, else STOP.

Object tracking is done to ensure that if a pellet does not move out of the New Object Area between frames, or a pellet moves back into the New Object Area.


Object Area from the center area, it will not be counted again. Pellets that are consumed while in the New Object Area would be counted. We have, however, noticed that salmon seldom consume pellets below 25 m of depth or at the cage bottom. The width of the New Object Area depends on the sampling frequency of the frames. As the sampling frequency is decreased, the width of the New Object Area must be increased. If the New Object Area is too narrow, a food pellet could enter the frame, and move through the new object area and into the center area between frames, and the algorithm would not count it. The wider the New Object Area, the greater the possibility of an error in the object count due to loss of track of a pellet. The width of the New Object Area is proportional to the maximum distance a food pellet can move between two frames.

Loss of track of a food pellet could occur in a number of situations. If a fish or other object moved between the camera and a food pellet between Frame $i$ and Frame $i + 1$, the pellet would not be visible in Frame $i + 1$, and a loss of track would occur. If a pellet fell out of range of the camera between Frame $i$ and Frame $i + 1$, the pellet would not be visible in Frame $i + 1$, and a loss of track would occur. In the first case, if the fish or other object moved out of the way between Frame $i + 1$ and Frame $i + 2$, the pellet would reappear in Frame $i + 2$. If the pellet reappeared in the central area of the frame at some later time, tracking would resume on the pellet through subsequent frames and no error in pellet count would occur. If however, the pellet reappeared in the New Object Area, the algorithm would not be able to differentiate the pellet from a new pellet entering the view, and would recount it. Therefore the New Object Area should be as narrow as possible in order to minimize the possibility of recounting error due to loss of track of objects. The use of a narrow New Object Area requires a high sampling frequency between frames, and consequently more processing power.

### Object matching algorithm

The object matching algorithm involves determining the movement of objects from Frame $i$ to Frame $i + 1$. This information can be used to determine if new objects have entered the view area of the camera in Frame $i + 1$.

The probability that two objects should be matched is measured by a distance function. The distance function can incorporate many measures such as straight line (Euclidean) distance, relative sizes of the objects, and direction of motion. The smaller the value of the distance function,


the ‘closer’ the two objects are, and the higher the probability that they should be matched. In Fig. 8, two frames, Frame $i$ and Frame $i + 1$ are shown with their respective objects. An overlay of Frame $i$ and Frame $i + 1$ is also shown, along with the desired matching result.

An object $O(i,n)$ in Frame $i$ is matched with an object $O(i + 1,m)$ in Frame $i + 1$ if:

$$
\text{distance}(O(i,n),O(i + 1,m)) \leq \text{distance}(O(i,n),O(i + 1,p)) \quad \forall O(i + 1,p) \in \text{Frame } i + 1
$$
(7)

$$
\text{distance}(O(i,n),O(i + 1)) \leq \text{distance}(O(i + 1,m)) \quad \forall O(i,q) \in \text{Frame } i
$$
(8)

$$
\text{distance}(O(i,n),O(i + 1,m)) < \text{a certain maximum distance}
$$
(9)

where the maximum distance is dependent on the maximum Euclidean distance a pellet can move between frame times (dependent on sampling frequency); $\forall$ means ‘for all’ and $\epsilon$ means ‘element of’.

The distance measure is composed of two individually weighted measures, the Euclidean distance ratio and the area ratio. As a result of the camera geometry, objects near the edge of the frame tend to move larger distances between frames than objects closer to the center of the frame. The maximum distance an object can move between frames as a function of position within the frame can be defined. This distance is used to prevent matching objects that are too far apart. The maximum distance is defined as follows:

$$
\text{maximum distance from center} = \text{Euclidean distance} ((x_c,y_c),(x_{\text{max}},0))
$$
(10)

where $(x_c,y_c)$ are co-ordinates of center of frame and $(x_{\text{max}},0)$ are co-ordinates of top right corner of frame.

The maximum movement for objects at the edge of the frame is $M_e$ and the maximum movement for objects at the center of the frame is $M_c$.

The maximum distance an object can move depending on position (distance from center—measured as the Euclidean distance from the

![](12_0.png)

Fig. 8. Object matching example.


center of frame to the centroid of the object in Frame i) within the frame is defined as:

$$
\text{Maximum distance} = \frac{(M_e - M_c) \times \text{distance from center}}{\text{maximum distance from centre}} + M_c
\tag{11}
$$

The Euclidean distance ratio is then defined as:

$$
\text{Euclidean distance ratio } E_r = \frac{\text{Euclidean distance}((x_i, y_i), (x_{i+1}, y_{i+1}))}{\text{maximum distance}}
\tag{12}
$$

where $(x_i, y_i)$ are co-ordinates of the object in Frame $i$ and $(x_{i+1}, y_{i+1})$ are co-ordinates of the object in Frame $i + 1$.

The area ratio, $A_r$, is the ratio of the area of the smaller object to the area of the larger object. For objects that should be matched, this ratio should be close to 1.0. The total distance measure is the weighted combination of the two distance measures.

$$
\text{distance} = \sqrt{(w_e E_r)^2 + (w_a (1.0 - A_r))^2}
\tag{13}
$$

where $E_r$, $A_r$ are the Euclidean distance ratio and area ratio, and $w_e$, $w_a$ are weightings for each component distance measurement, respectively.

### Validation experiment

The manual method and the automatic counting algorithm were tested on image sequences acquired in a commercial Atlantic salmon sea cage near Port McNeill, BC, and in chinook salmon experimental sea cages at the Department of Fisheries — Pacific Biological Station in Nanaimo, B.C. Food pellets used were 9-5 mm in diameter. Image sequences were captured in sea cages with and without fish.

The image sequences used as input were designed to approximate the pellet densities occurring in actual feeding situations. These densities were calculated from standard feeding tables (Source: White Crest Mills, 1993). Table 1 shows the approximate number of food pellets entering the view area of the camera per min for different pen densities (number of kg of fish per m³ of water). According to standard feeding tables, in water at 16°C, 800 g fish should be fed 1.55% of their body weight per day using 9.5 mm food pellets (Source: White Crest Mills, 1993). These calculations assume a 9.5 mm food pellet can be detected up to 1.5 m.


Detection and counting of feed pellets in a sea cage

from the camera (camera coverage area is 5·6 m²), a net pen size of 15 m by 15 m and 21 m deep, and a uniform food pellet distribution.

RESULTS AND DISCUSSION

The maximum coverage of the camera depends on the pellet size used and the resolution of the video camera. Table 2 shows the theoretical

TABLE 1  
Number of Food Pellets Entering Camera View per Minute

| Pen density kg|m³ | Number 800 g fish in pen | Mass of 9·5 mm feed per day (kg) | Number of pellets per day for entire pen | Number of pellets passing camera per day (none eated) | Pellets/min passing camera (4 h feeding) (none eaten) |
|---------------|----------------------------|-------------------------------|-----------------------------------------|------------------------------------------------------|-----------------------------------------------------|
| 5             | 30 972                     | 384                           | 345 646                                 | 12 914                                              | 54                                                  |
| 6             | 37 166                     | 460                           | 414 775                                 | 15 496                                              | 65                                                  |
| 7             | 43 360                     | 537                           | 483 904                                 | 18 079                                              | 75                                                  |
| 8             | 49 554                     | 614                           | 553 034                                 | 20 662                                              | 86                                                  |
| 9             | 55 749                     | 691                           | 622 163                                 | 23 244                                              | 97                                                  |
| 10            | 61 943                     | 768                           | 691 292                                 | 25 827                                              | 108                                                 |
| 11            | 68 137                     | 844                           | 760 421                                 | 28 410                                              | 118                                                 |

TABLE 2  
Theoretical Area of Objects in Pixel Units vs Distance from Object to Camera

| Object area (mm²) (Approximate pellet size) | Distance from object to camera (m) (camera coverage area (m²)) |
|---------------------------------------------|----------------------------------------------------------------|
|                                             | 0·50 | 0·75 | 1·00 | 1·25 | 1·50 | 1·75 | 2·00               |
|                                             | (0·62) | (1·4) | (2·5) | (3·9) | (5·6) | (7·6) | (10·0)     |
| 1·00 (1 mm)                                  | 0·42 | 0·19 | 0·11 | 0·07 | 0·05 | 0·03 | 0·03               |
| 4·00 (2 mm)                                  | 1·69 | 0·75 | 0·42 | 0·27 | 0·19 | 0·14 | 0·11               |
| 9·00 (3 mm)                                  | 3·79 | 1·69 | 0·95 | 0·61 | 0·42 | 0·31 | 0·24               |
| 16·00 (4 mm)                                 | 6·74 | 3·00 | 1·69 | 1·08 | 0·75 | 0·55 | 0·42               |
| 25·00 (5 mm)                                 | 10·5 | 4·68 | 2·63 | 1·69 | 1·17 | 0·86 | 0·66               |
| 36·00 (6 mm)                                 | 15·2 | 6·74 | 3·79 | 2·43 | 1·69 | 1·24 | 0·95               |
| 49·00 (7 mm)                                 | 20·7 | 9·18 | 5·16 | 3·30 | 2·29 | 1·69 | 1·29               |
| 64·00 (8 mm)                                 | 27·0 | 12·0 | 6·74 | 4·32 | 3·00 | 2·20 | 1·69               |
| 81·00 (9 mm)                                 | 34·1 | 15·2 | 8·54 | 5·46 | 3·79 | 2·79 | 2·13               |
| 100·00 (10 mm)                               | 42·2 | 18·7 | 10·5 | 6·74 | 4·68 | 3·44 | 2·63               |


area of objects imaged by the camera in pixel units corresponding to different object-camera distances (512 x 480 pixel image, view angle of camera — 76°52'). In practice, these areas are approximately 1-2 pixels larger due to either light scattering, system resolution or system response.

Table 3 shows the results of using the computer algorithm to count 9-5 mm food pellets falling through the view area of the camera. A set of 25 frames sampled at approximately four frames per s were used for each test. In tests 1-10, food pellets were falling past the camera at a rate of approximately 120 pellets per min. In tests 11-18, food pellets were falling past the camera at a rate of approximately 200 pellets per min. There were no fish in the water during these tests.

It should be noted that the overall error information is not very significant. Certain errors can cause the computer count to be too low, and other types of errors can cause the computer count to be too high. These two types of error can cancel each other out, and produce a misleading overall error measurement. This is the case in test 1. The number of errors the computer algorithm made for each test is a more significant

**TABLE 3**  
Results of Counting Trials

|   | Actual food pellet count | Computer food pellet count | Number of counting errors | Overall error in computer count |
|---|--------------------------|----------------------------|---------------------------|---------------------------------|
| 1 | 8                        | 8                          | 2                         | 0%                              |
| 2 | 14                       | 16                         | 2                         | +14.29%                         |
| 3 | 15                       | 15                         | 4                         | 0%                              |
| 4 | 11                       | 11                         | 2                         | 0%                              |
| 5 | 14                       | 13                         | 1                         | -7.14%                          |
| 6 | 12                       | 10                         | 2                         | -16.67%                         |
| 7 | 10                       | 13                         | 4                         | +30.00%                         |
| 8 | 18                       | 17                         | 3                         | -5.56%                          |
| 9 | 9                        | 12                         | 3                         | +33.33%                         |
| 10| 12                       | 14                         | 2                         | +16.67%                         |
| 11| 23                       | 24                         | 2                         | +4.35%                          |
| 12| 26                       | 24                         | 2                         | -7.69%                          |
| 13| 22                       | 20                         | 4                         | -9.01%                          |
| 14| 17                       | 19                         | 2                         | +11.76%                         |
| 15| 20                       | 21                         | 3                         | +5.00%                          |
| 16| 20                       | 20                         | 2                         | 0%                              |
| 17| 23                       | 21                         | 2                         | -8.70%                          |
| 18| 23                       | 21                         | 2                         | -8.70%                          |


Detection and counting of feed pellets in a sea cage

indication of the accuracy of the algorithm. It is important to determine what kinds of errors occurred. Table 4 shows the frequencies of different types of errors that occurred in the 18 tests that were conducted.

Errors in object detection were a major cause of error in the computer count. Many of these errors were caused when food pellets fell too close to the front of the camera. The camera blocked the light reaching the pellet, and therefore the pellet was not detected. By adding a transparent shield around the camera, pellets will not fall too close to the front of the camera, and the frequency of this type of error should be reduced.

For the majority of images used in the tests, the automatic threshold determination algorithm accurately separated objects in the image from the background.

Object division was another major cause of counting errors. A more detailed study into determining the values of the constants used for curvature adjustment may be necessary.

The object classification algorithm developed did not accurately classify some valid pellet objects. In additional experiments with fish in the sea cage, the classifier did not accurately classify the non-pellet objects. Non-pellet objects such as fish will be present in an actual feeding situation. One possible solution would be to use additional information such as the original gray levels of the object to improve the classifier. Another solution would be to enclose the view area of the camera in a netted structure to prevent fish from entering the view area. This would likely eliminate the need for more complicated object classification.

Object tracking could likely be improved by increasing the frame sampling rate. If objects move smaller distances between frames, object tracking will become less error prone. This adjustment will also reduce

---

![TABLE 4](16_0.png)

Frequency of Occurrence of Different Counting Errors

| Cause of counting error | Number of occurrences | % of total errors |
|-------------------------|-----------------------|------------------|
| Incorrectly tracking an object | 12 | 27.27% |
| Classifying a valid pellet as a non-pellet object | 11 | 25.00% |
| Incorrectly failing to divide/dividing an object | 9 | 20.45% |
| Error in object detection | 7 | 15.91% |
| Valid pellet object moved through New Object Area between frames and was therefore undetected | 3 | 6.82% |
| Classifying a non-pellet object as a valid pellet object | 2 | 4.55% |


errors which occurred when an object moved through the New Object Area between frames, and was therefore undetected. Increasing the sampling rate would require more processing power, but would likely result in higher object matching accuracy. Additional components could be added to the distance measure, and investigations should be carried out to determine the best weighting scheme to use for the distance measure.

During the course of this investigation it was noted that when fish are in the sea cage, the light reaching the camera may be insufficient to illuminate the food pellets enough to be detected by the camera. A large number of fish above camera level greatly reduce the available illumination. An underwater light source could be attached to the camera, or a more light sensitive camera could be used to resolve this problem. The use of a high resolution digital camera (more pixels per frame) would improve the accuracy of many algorithms used in the pellet counting process. By switching to a digital camera, the quality of the image sequences used for analysis would be higher, and the need for the video equipment could be eliminated.

## CONCLUSION

In order to automate the counting of food pellets, image analysis algorithms were developed to detect and classify objects, track pellets from one frame to another, and count the number of food pellets passing through the view area of the underwater camera. The average counting accuracy of the automatic algorithms was ±10%. Improvements to the algorithms were suggested that should reduce this error. The algorithms which were developed for this project represent the first stage in the development of a commercial automatic pellet counting system. Future work will focus on reducing the count error of the automatic system.

## ACKNOWLEDGEMENTS

This work has been supported by B.C. Packers Ltd; Pacific Biological Station — Fisheries and Oceans Canada; and funded by the Natural Sciences and Engineering Research Council, Canada.

## REFERENCES

Austreng, E., Storebakken, T. & Åsgård, T. (1987). Growth rate estimates for cultured Atlantic salmon and rainbow trout. *Aquaculture, 60*, 157-60.


Detection and counting of feed pellets in a sea cage

Duda, R. O. & Hart, P. E. (1973). *Pattern Classification and Scene Analysis*. John Wiley and Sons, New York.

Juell, J. (1991). Hydroacoustic detection of food waste—a method to estimate maximum food intake of fish populations in sea cages. *Aquacult. Engng, 10*, 207-17.

Juell, J. E., Furevik, D. M. & Bjordal, Å. (1993). Demand feeding in salmon farming by hydroacoustic food detection. *Aquacult. Engng, 12*, 155-67.

Poon, S., Ward, R. K. & Palcic, B. (1992). Automated Image Detection and Segmentation in Blood Smears. *Cytometry, 13*, 766-74.

Pratt, W. K. (1991). *Digital Image Processing*. John Wiley and Sons, New York, pp. 449-84, 597-605.

Seymour E. A. & Bergheim, A. (1991). Towards a reduction of pollution from intensive aquaculture with reference to the farming of salmonids in Norway. *Aquacult. Engng, 10*, 73-88.

Shepherd, J. S. & Bromage, N. (1988). *BSP Professional Books*. Oxford University Press, Oxford, pp. 78-81.

Storebakken, T. & Austreng, A. (1987). Ration level for salmonids 1. Growth, survival, body composition, and feed conversion in Atlantic salmon fry and fingerlings. *Aquaculture, 60*, 189-205.

Thorpe, J. E., Talbot, C., Miles, M. S., Rawlings, C. & Keay, D. S. (1990). Food consumption in 24 hours by Atlantic salmon (*Salmo salar L.*) in sea cage. *Aquaculture, 90*, 41-7.
