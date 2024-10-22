# Page 1

ComputersandElectronicsinAgriculture201(2022)107335
Contents lists available at ScienceDirect
Computers and Electronics in Agriculture
journal homepage: www.elsevier.com/locate/compag
Review
Recent advances of target tracking applications in aquaculture with
emphasis on fish
Yupeng Meia,b,c,d, Boyang Suna,b,c,d, Daoliang Lia,b,c,d,f, Huihui Yue, Hanxiang Qina,b,c,d,
Huihui Liua,b,c,d, Ni Yana,b,c,d, Yingyi Chena,b,c,d,e,*
aNational Innovation Center for Digital Fishery, China Agricultural University, Beijing 100083, PR China
bKey Laboratory of Smart Farming for Aquatic Animal and Livestock, Ministry of Agriculture and Rural Affairs, Beijing 100083, PR China
cBeijing Engineering and Technology Research Centre for the Internet of Things in Agriculture, China Agricultural University, Beijing 100083, PR China
dCollege of Information and Electrical Engineering, China Agricultural University, Beijing 100083, PR China
eSchool of Information Science and Technology, Beijing Forestry University, Beijing 100083, PR China
fYantai Research Institute of China Agricultural University, Yantai 264670, PR China
A R T I C L E I N F O A B S T R A C T
Keywords: In aquaculture, Behavioral monitoring of fish contributes to scientific management and reduces the threat of loss
Target tracking from disease and stress. Fish tracking technology plays an important role in behavior monitoring. It can pay
Fish behavior attention to the movement of fish at any time and discover various abnormal behaviors in time. As a non-invasive
Correlation filter
method, computer vision is a powerful tool for fish tracking.. Its tracking principle is to establish the relationship
Siamese networks
between fish positions in a continuous video sequence and get the complete movement trajectory of the fish.
Deep learning
Nevertheless, computer vision modeling used for fish tracking is riddled with many challenges, such as fish
deformation, frequent occlusion, scale change, etc. Around these difficult issues, many scholars have carried out
the research. In this paper, we review the progress of tracking algorithms in fish research. Then, methods for fish
tracking before deep learning are introduced. Further, a detailed discussion of fish tracking methods employing
deep learning such as tracking-by-detection, deep features combined with correlation filtering methods, Siamese
networks, etc. Furthermore, we summarize datasets that can be used as fish tracking and give evaluation metrics
in target tracking algorithms. In addition, experimental data of several mainstream tracking algorithms on a
public tracking dataset are given. Finally, we discuss the outstanding findings and look forward to the fish
tracking method combined with Transformer, aiming to provide a reference for accelerating the promotion of
smart fishery and precision farming.
1. Introduction fish tracking methods can be applied in precise feeding, disease diag-
nosis, counting and broodstock tracking (Zhao et al., 2016). In summary,
Target tracking is an important branch of computer vision. It is fish tracking technology is of great significance in aquaculture man-
widely used in video surveillance and other fields (Li and Du, 2021; Pan agement decision making.
et al., 2017), and will be widely used in aquaculture in the future. In At present, many technologies were used to track fish, such as
aquaculture, fish tracking technology is an important way of monitoring computer vision (Rodríguez et al., 2015), acoustics (Pursche et al., 2014)
behavior. By tracking the fish, it is possible to monitor the growth and and sensors (Hedgepeth et al., 2000). Acoustic technology requires the
behavior of fish (Saberioon et al., 2017), helping the aquaculture in- placement of a small photoacoustic tag in the abdominal cavity of the
dustry to make the best use of resources (Yue and Shen, 2022). At the fish (or attached to the outside of the fish) for accurate tracking of the
same time, tracking fish and analyzing their behaviors can monitor the fish’s trajectory (Fig. 1). The ultrasonic signals emitted by the tags are
environmental conditions for their growth (Bianchi et al., 2019). It can received by hydrophones placed at specific locations underwater (Hou
also better control water quality, assess the welfare of cultured fish and et al., 2019). Acoustics are widely used for spatio-temporal distribution
deals with abnormal behavior on time (Martins et al., 2012). In addition, behavior, species detection, fish stock assessment (Mizuno et al., 2015)
* Corresponding author at: China Agricultural University, 17 Tsinghua East Road, Beijing 100083, PR China.
E-mail address: chenyingyi@cau.edu.cn (Y. Chen).
https://doi.org/10.1016/j.compag.2022.107335
Received 4 April 2022; Received in revised form 13 July 2022; Accepted 22 August 2022
Availableonline30August2022
0168-1699/©2022ElsevierB.V.Allrightsreserved.

# Page 2

Y. Mei et al. C o m p u t e r s a n d E l e c t r o n ic s i n A g r i c u l t u r e 201(2022)107335
and fish tracking (Pursche et al., 2014) without stressing the fish. outlined in Fig. 3. Section 2 briefly describes common key challenges in
However, acoustic methods are susceptible to noise, and their high cost, fish tracking. Section 3 introduces various tracking methods for fish
technical difficulty, etc. further limit their applications (Saberioon and before deep learning, such as Kalman filtering methods, meanshift,
Cisar, 2016). A variety of sensors based on different parameters can be correlation filtering. Section 4 presents various tracking methods for fish
used to monitor, identify and assess fish behavior. Various kinematic using deep learning, such as Tracking-by-detection, Depth features
parameters of the fish can be determined by implanting components combined with correlation filtering, End-to-end tracking method, Sia-
such as accelerometers, and the sensors can also be fixed to the fish by mese Network. Section 5 summarizes the datasets available for fish
other means (An et al., 2021). However, with modern aquaculture tracking and gives evaluation metrics for target tracking algorithms. In
increasingly dominated by welfare farming, this invasive monitoring addition, experimental data of several mainstream tracking algorithms
method is unlikely to be suitable for large-scale intensive farming (Li on public tracking datasets are given. Section 6 describes the application
et al., 2020a). In contrast, computer vision technology has many ap- of tracking methods in fish research. Section 7 presents a discussion and
plications in aquaculture. The use of computer vision for tracking, outlook based on the results of this review, providing researchers with
monitoring, size and quality estimation of fish allows for more accurate future directions.
and rapid measurements, saving a lot of manpower and material re-
sources (Vo et al., 2021). The development of machine vision has led to 2. Challenges in fish tracking
smart fishery as a new generation of aquaculture model. This model can
manage and monitor all aspects of fish growth conditions and the Fast, accurate and robust tracking of fish has always been a challenge
aquaculture environment, with functions such as real-time data collec- in the tracking of fish video targets. Problems such as occlusion between
tion and remote monitoring of production bases. It promotes the deep fish (Xiao et al., 2017; Mao et al., 2015), fish deformation (size, shape,
integration of digital technology and fishery production (Ebrahimi et al., pose and orientation can be arbitrary at any time) (Spampinato et al.,
2021). A fish image acquisition system using machine vision was 2014), and uneven illumination make the video frames highly differ-
designed by the author (Han et al., 2020) to achieve all-round acquisi- entiated. This poses new challenges for the generalization of fish video
tion of fish behavior (Fig. 2). tracking algorithms. There is currently no single method that solves all
In recent years, target tracking using machine vision has formed a of these problems. In this paper, we summarise the difficulties faced in
more complete technical system from data acquisition, data set con- realistic environments for fish tracking (Yang et al., 2021), as shown in
struction, data pre-processing, target identification, target tracking to Fig. 4, which mainly include:
technology application (Anas et al., 2020). However, the tracking of fish
still faces many difficulties. When fish move underwater, problems such • Occlusion: The relative movement of fish to each other often results
as mutual occlusion, morphological changes and abnormal water quality in occlusion. Occlusion can be divided into partial and total occlu-
often occur, which will lead to failure of fish tracking (Lumauag and sion, where partial occlusion retains some of the feature information
Nava, 2018). Failure to track fish effectively will seriously affect the by which the fish can still be tracked. Total occlusion means that the
analysis of their behavior and pose great challenges to subsequent target is completely occluded and all features are lost, which will
research and management of fish. On the contrary, if fish can be accu- result in a failure to track the target.
rately, real-time and effectively tracked, various behavioral changes in • Morphological change: Because fish is non-rigid, there will be some
fish swimming can be obtained. By identifying abnormal behaviors in deformation in the process of movement, which will lead to changes
time (Xu et al., 2020a), problems such as disease (An et al., 2021), water in its characteristics and appearance model, and easily lead to
quality (Xia et al., 2018), feeding (Zhou et al., 2018a) and biomass tracking failure.
estimation (Li et al., 2020b) can be solved in fish farming. Then, the • Scale change: Due to the movement of fish, the size of the area it
system provides corresponding solutions for the problem. Finally, to occupies in the image changes. Scale adaptive tracking can solve
achieve refined breeding, reduce the waste of human and material re- these problems and avoid tracking failure.
sources and economic losses (Anas et al., 2020). In conclusion, achieving • Background interference: During fish tracking, fish may resemble the
efficient tracking of fish plays an important role in the development of surrounding background, such as color, shape, texture, etc., which
refined aquaculture, and it is also of great significance to promote the can easily cause misjudgment by the tracker and lead to tracking
development of smart fisheries. failure.
Research and development of fish tracking methods using machine • Image blur: In a real aquaculture environment, the rapid swimming
vision are still limited. There is still relatively little literature that pro- of fish can cause significant blurring of the video image, making it
vides a systematic analysis of fish tracking methods. Therefore, we re- difficult to distinguish by appearance and leading to tracking failure.
view methods for fish tracking, the main algorithmic elements are
Fig. 1. Signal tag is placed in fish’s abdominal cavity (left) or attached externally (right).
2

# Page 3

Y. Mei et al. C o m p u t e r s a n d E l e c t r o n ic s i n A g r i c u l t u r e 201(2022)107335
Fig. 2. Adopting top-view camera and underwater to catch fish behavior in three-dimensions.
Fig. 3. The fish tracking methods in the overview.
• Environmental change: Changes in illumination, camera resolution, fundamental and important processing link in intelligent video analysis
current circulation in marine aquaculture and water turbidity are systems (Yazdi and Bouwmans, 2018). When target detection of moving
important factors affecting fish tracking. fish, effective segmentation of the moving areas in the image can be used
to obtain more accurate information about the fish’s movement and
3. Fish tracking algorithms before deep learning reduce the difficulty of tracking, identifying and analysis of the fish in
subsequent stages. The tasks and results of fish detection are shown in
With the rapid development of artificial intelligence and other Fig. 5. In general, detection methods for moving targets fall into the
related scientific theories (Li et al., 2021; Tang et al., 2021), motion following categories: inter-frame differencing (Sengar and Mukho-
target detection and tracking technology have become a research hot- padhyay, 2017), background differencing (He et al., 2018) and optical
spot in the field of computer vision. It is widely used in the fields of flow methods (Delpiano et al., 2016). In this section, we introduce the
intelligent robotics and intelligent aquaculture. The purpose of moving moving target detection algorithm in detail, and give the accuracy,
target detection is to extract changing areas from the background from recall and other performance data of each algorithm, as shown in
the video sequence. In the process of fish detection, the size, position and Table 1. We objectively describe each algorithm and give the moving
direction of movement of the fish are further determined, so that the fish detection scenarios suitable for these algorithms.
changing areas in the video image sequence are detected and the fish are
extracted from the background image. The purpose of target tracking is 3.1.1. Interframe difference method
similar to that of moving target detection. It is to obtain the location or Inter-frame differencing is a method of obtaining a moving target
presence of the target in the image at the current moment, except that profile by differencing two adjacent frames in a video image sequence
target tracking needs to maintain the temporal consistency of the target. (Sengar and Mukhopadhyay, 2017). Set fk(x,y)to denote the pixel value
Motion target tracking is based on motion target detection and uses the of the pixel point (x,y)in the frame k and fk+1(x,y)to denote the pixel
extracted motion information to find the position in successive frames value of the pixel point with position information (x,y)in the framek+
that matches the target’s features, ultimately obtaining the complete 1. Thus, the principle equation is shown in Equation (1).
motion trajectory of the motion target. {
D k(x,y)=
1 0,
,
if|f k+1(x, oy t) h(cid:0) ersf k(x,y)|〉T
(1)
3.1. Fish movement target detection
If the difference result of the image is greater than the selection
Motion target detection, also known as foreground detection, is a threshold (for binary images), then it is defined as the foreground.
3

# Page 4

Y. Mei et al. C o m p u t e r s a n d E l e c t r o n ic s i n A g r i c u l t u r e 201(2022)107335
Fig. 4. The images above illustrate the various challenges faced in fish tracking (Wang et al., 2019; Hsiao and Chen, 2016; Beyan et al., 2018; Boom et al., 2012).
Fig. 5. A flow chart of moving target detection (Shiau et al., 2013).
Table 1
Representative works of commonly used motion target detection algorithms. ACC: accuracy, PRE: precision, REC: recall, FM: F-measure, FPR: false positive rate.
Reference Approach Dataset Performance Suitable for scenarios in fish research
Sengar and Interframe difference Durlacher-Tor ACC: 93.99 %1 Fish without static and occlusion
Mukhopadhyay, 2017
Goyal and Singhai, 2018 Gaussian mixture CDnet PRE: 70.12 %; REC: 71.08 %; FM: Fish detection in relatively complex environments
background modeling 66.24 %
Yang et al., 2018b Codebook model modeling LS test image PRE: 85 %; REC: 95 %; FPR: 51 % Fish detection in relatively complex environments
set
Yang et al., 2018a Visual background extractor Pedestrians PRE: 94.58 %; REC: 69.78 %; FM: Fish detection in relatively complex environments
80.13 %
Zhang et al., 2018 Optical flow method KITTI2015 PRE: 74.3 %; REC:85.8 %; FPR: 1.2 In dense scenes with small water surface fluctuations or
%; FM: 79.0 % filming the camera movement of fish
Conversely, it was classified as the background. When the fish is moving, authors (Lan et al., 2014) propose a fast detection and identification
the background is almost stationary or only slightly moving in the whole method for moving robot fish, which can detect fish and determine their
image except for the movement of the fish, using the inter-frame dif- movement accurately, completely and quickly. Sengar and Mukho-
ference method to get the difference of each frame and selecting the padhyay (2017) mentioned the inter-frame difference method and
threshold segmentation to get the area of the fish body. Using the three- conducted experiments on challenging video surveillance dataset se-
frame differential method and the background differential method, the quences. It can be seen from experiments that the accuracy of this
4

# Page 5

Y. Mei et al. C o m p u t e r s a n d E l e c t r o n ic s i n A g r i c u l t u r e 201(2022)107335
method on three video data reaches 94.46 %, 97.96 % and 93.99 % (ii) it is also somewhat inadequate for systems with high real-time
respectively, which has high detection accuracy. The inter-frame dif- requirements, and there are some “ghosting” phenomena.
ference method is relatively simple and easy to implement, so it is
suitable for fish without static and occlusion. However, it has the 3.1.2.2. Codebook model. To perform accurate detection of color video
following disadvantages (Enze and Miura, 2020): images, the idea of clustering is introduced into the background
modeling method and a codebook model is proposed (Kim et al., 2005).
(i) When the moving speed of the target is too fast, the overlapping An initial codebook model is created for each pixel point in the scene
degree of the target contour is large, which is easy to cause the based on successive input color and luminance values. This codebook
phenomenon of “ghosting”. “Ghosting” usually refers to the model contains several codewords, and the codebooks of all points form
appearance of a double image of a target in an image. Here, it a complete background model. During motion target detection, the
refers to the phenomenon that the motion target detected by the current pixel point is compared one by one with the established code-
frame difference method is an overlap of two targets when the word, and if the match is successful, the point is considered to be a
positions of the motion targets are significantly different in background point, otherwise, it is a foreground point (Yang et al.,
adjacent frames. 2018b). To improve fish recognition performance, Wang et al. (2017a)
(ii) When the moving speed of the target is too slow, the detection of used a two-level codebook to represent the importance between a local
the target may be incomplete, and the phenomenon of “hollow” descriptor and each codeword in its corresponding k-nearest neighbor.
may appear. In other words, The position of the moving target in After coding, a shrinkage function is introduced to shrink the irrelevant
the image has changed, but the gray value of the corresponding coefficients, achieving significant performance improvements in fine-
pixel is the same, resulting in a difference result of 0, so it is grained fish recognition tasks. This codebook-based background model
misjudged as the background, resulting in the appearance of the can detect multimodal backgrounds in real-time and can perform mo-
“hollow” phenomenon. tion detection for long periods with limited memory, but it requires a
long video sequence to train the codebook before it can perform motion
3.1.2. Background difference method detection, which requires a large amount of memory.
The background differencing method is a differencing operation
performed on a sequence of video images. The subject of the differencing 3.1.2.3. Visual background extractor. The visual background extractor
operation is the current frame and the background frame obtained in (ViBe) algorithm is a universal background subtraction algorithm pro-
advance or the background image obtained by real-time update. The posed by Barnich and Droogenbroeck (Barnich and Droogenbroeck,
resulting difference map is then thresholded to extract the moving tar- 2009). The principle is shown below (Yang et al., 2018a):
gets in the image (Xiao et al., 2005). The core idea of this algorithm lies Fig. 6 shows the Euclidean space(C1,C2). Here, M(x)={v(1),v(2),v(3),
in the creation of a background model. ⋯,v(m)} is the background template of a pixelx, N is the number of
It has been used to extract foreground targets to track fish and to samples in the template, and v(x)is the value ofx . The range is a radius R
a (Zn ha oly us e
e
tt ah le .i
,
r
2
b 0e 0h 8a ).v i To hr
i
sb my ele thar on di n cg
a
nb ba ec k ug sr eo du n tod ds et ta et cis tt i fic sa hl ii nn f ro er lm ata ivti eo ln
y
calledSR(v(x)). The goal is to determine whether x is a background pixel.
complex environments. Common background modeling methods are the
The intersection of SR(v(x))and M(x)={v(1),v(2),v(3),⋯,v(m)}is denoted
as follows:
gaussian mixture model (Dell et al., 2014), codebook model (Kim et al.,
2005) and visual background extraction model (Qu and Huang, 2017). {S R(v(x))∩{v(1),v(2),v(3),⋯,v(m)}} (2)
3.1.2.1. Gaussian mixture model. The basic idea of the Gaussian mixture
when there are ViBe thresholded samples in SR(v(x)), x is the back-
ground pixel.
model is to assume that the distribution of all pixels is composed of some
The traditional background difference classification detection
single Gaussian model, and update the model parameters with new pixel
method usually needs to re-consume a sequence of frames for initiali-
values (Zivkovic, 2004). Then, according to the set standard, whether a
zation when the image background changes suddenly. The ViBe algo-
pixel belongs to the background or the prospect is determined. Finally,
rithm solves the above problems and improves the overall adaptability
complete the detection of moving targets (Li et al., 2017). To overcome
and real-time performance of the algorithm. It is more suitable for
the challenges that exist due to environmental variations in luminosity,
detection tasks in complex environments. Various non-intrusive auto-
fish camouflage, dynamic backgrounds, water turbidity, low resolution,
matic fish counters based on principles such as resistivity, light beams
shape distortion of swimming fish, and subtle differences between
and sonar are often unable to distinguish between fish and other passing
certain fish species. Many scholars have combined the Gaussian mixture
objects, and cannot identify different species. To address this situation,
model method with fish detection and achieved good results (Salman
Shevchenko et al. (2018) propose a framework for detecting fish in low-
et al., 2019; Shiau et al., 2013; Hossain et al., 2016). To further improve
the detection performance of the model, the Gaussian mixture model is
combined with the YOLO algorithm. Then, the Gaussian mixture model
and the time information obtained from the optical flow were used to
classify the fish species hidden in the background and moving freely,
achieving high accuracy (Jalal et al., 2020). In addition, Gaussian
mixture model methods are widely used for real-time fish target detec-
tion (Li et al., 2014), counting (Sharif et al., 2016), etc. It experimented
on the CDnet dataset (Goyal and Singhai, 2018), and the experimental
results are shown in Table 1. Overall, the GMM algorithm can update the
background adaptively, accurately detecting any moving targets in the
background, and is not very computationally intensive. But it has the
following disadvantages:
(i) it is very sensitive to sudden changes in light intensity in the
background;
Fig. 6. Operating principle of the ViBe algorithm.
5

# Page 6

Y. Mei et al. C o m p u t e r s a n d E l e c t r o n ic s i n A g r i c u l t u r e 201(2022)107335
visibility, noisy underwater video, where the ViBe method performs test of an underwater fish is carried out in a tank, and the experiment
better in terms of noise resistance and adaptation to light. However, the proves that this method can also avoid the interference of side glass
algorithm relies heavily on the initial frame and is prone to “ghosting” reflection and water surface fluctuation (Yi and Chen, 2019). In the
when there is a moving foreground in the initial frame. underwater environment, there are conditions such as low visibility
(Gaude and Borkar, 2019) and abnormal water quality (Zhao et al.,
3.1.3. Optical flow method 2019), which pose difficulties for the detection and tracking of moving
The optical flow method represents the motion field in the current fish targets. To solve this problem, fish targets need to be detected. Then,
video sequence by the motion vector of the pixel point. It can be used to Kalman filter is used to estimate the motion state of fish. Finally, the fish
detect moving objects (Barron et al., 1994). The optical flow method has tracking is realized by using the frame relation matrix. Kalman filter
high precision and can accurately analyze fish. It is suitable for detecting algorithm is simple, with low computational complexity and high ac-
scenes where only the foreground is moving or both the foreground and curacy. Good for tracking fish in simple scenarios. However, when fish
background are moving (Shin and Musunuri, 2017; Terayama et al., have irregular movement and cross occlusion, Kalman filter will diverge,
2015). Lee et al. (2020) used the optical flow method and the boundary resulting in failure of fish moving target tracking.
detection algorithm for the location detection of machine fish. The
method was validated and achieved good results. Zhang et al. (2018) 3.2.2. Particle filter
tested the optical flow method on the datasets Cdnet2014, KITTI2015 The Kalman filter has a limited range of applications and is only
and MPI Sintel. Among them, on the KITTI2015 dataset, the precision applicable to linear systems. However, many factors may lead to non-
rate reaches 74.3 %, and the recall rate is 85.8 %. The method has the linear, non-Gaussian distributions during the tracking of fish. To
ability to obtain the position and velocity information of the moving address this problem, particle filtering has been proposed (Isard and
target. It is suitable for situations where the camera is moving or where Blake, 1998; Breitenstein et al., 2011). It compensates for the small
you need to know the position and speed of the fish. applicability of the Kalman filter and can solve the non-linear problems
However, in the actual farming scene, the distribution of pixel vector caused during fish tracking (Xiao et al., 2011). Jiang et al. (2013)
information in the optical flow field is easily affected by light changes, investigated a new matching function for tracking the movement of koi
background interference and noise interference. Hence, the algorithm is in water using particle filters. Terayama et al. (2017) proposed a method
less resistant to interference. In addition, the optical flow method needs to measure fish motion characteristics using particle filtering. For fish
to analyze each pixel at the same time to calculate the information of the that are flexible and easy to move, uncertain in movement, similar in
velocity vector, which makes the complexity of the algorithm high. appearance, and frequently occluded. Cong et al. (2016) used particle
Therefore, this method cannot be applied to systems with high real-time filtering to approximate the uncertainty of zebrafish motion and built an
requirements. efficient hybrid motion model to predict its position. Finally, the effec-
tive tracking of zebrafish is realized.
3.2. Fish movement target tracking
3.2.3. Meanshift
Target tracking is a widely used element in the field of computer The Meanshift algorithm (Park, 2021) is one of the kernel methods
vision. To track the moving target, the target must be effectively and has a wide range of applications. The main idea is to use the opti-
expressed first. Then find the most similar area to the target in each mization principle of the steepest descent method to gradually iterative
frame of the next video sequence to determine the location of the target the objective function along the gradient descent direction until the
in the current frame. For fish tracking, the research on fish moving target optimal solution is obtained. In the application of target tracking, it is to
tracking algorithms is more challenging due to the non-rigidity of fish find the candidate interval with the highest similarity (Jang and Jiang,
and the problems of occlusion, rotation, and scale changes during fish 2021). The basic principle of the Meanshift tracking algorithm (Shi and
movement (Wang et al., 2017c). The commonly used traditional target Xiang, 2013) is to determine the next position of the moving target by
tracking algorithms mainly include the Kalman filter (Li et al., 2016), judging the similarity of two corresponding templates. Then, the new
particle filter (Pinkiewicz et al., 2008), Meanshift algorithm (Park, center point position is found according to the iterative method, and the
2021) and correlation filtering algorithm (Bolme et al., 2010). final result is the new position point of the moving target (Fig. 7). The
following are the basic steps of Meanshift (Yao, 2021).
3.2.1. Kalman filter Step 1: Target template creation: Calculate the probability density qu
To solve the linear filtering problem for discrete data, Kalman pro- of the target template:
p tho es e fid
e
lt dh e
o
fK ta al rm ga en
t
tfi ralt ce kr
i
na glg (o Lr ii t eh tm
a
li .n
,
21 09 16 60 ),
.
w Thh eic Kh
a
w lmas
a
nla fite lr
te
e rx it se n
a
d lie nd
e
ato
r q
u=C∑n k(⃦ ⃦ ⃦x(cid:0) hx i⃦ ⃦ ⃦2)
δ[b(x i)(cid:0) u] (3)
filtering and prediction algorithm that can effectively predict the posi- i=1
tion of a target. It can predict the estimated position of a moving target where C is the normalization factor and k denotes the kernel func-
at the next moment with relative accuracy (Liu et al., 2011; Shantaiya tion. The Epanechikov kernel function is used in this algorithm, and the
et al., 2015).
The algorithm consists mainly of a prediction part and a parameter
update part. In the prediction phase, the state values and errors esti-
mated at the previous moment are used to predict the state values and
errors at the next moment. In the update phase, the predicted states and
the current moment’s observations are combined to estimate the best
result (Zhou et al., 2016).
Kalman filtering methods are commonly used in fish target tracking
tasks (Huang et al., 2019; Jing et al., 2017). For situations where oc-
clusion often occurs between moving fish, the Kalman filter method is
used to predict the fish’s position based on their kinematic information.
Then, the trajectory of each fish is connected between frames to achieve
the tracking effect (Barreiros et al., 2021; Zhu et al., 2020). In a complex
environment with obstacle occlusion and light reflection noise, the
Kalman filtering method is used for tracking. Then, the visual tracking Fig. 7. Operating principle of the Meanshift algorithm.
6

# Page 7

Y. Mei et al. C o m p u t e r s a n d E l e c t r o n ic s i n A g r i c u l t u r e 201(2022)107335
δ function is used to determine whether point x belongs to the target improved Meanshift algorithm combined with Kalman filtering. The
region. improved algorithm tracked the target more accurately and the trajec-
Step 2: Search for models: In the subsequent series of frames, the tory of the tracked target was more continuous. Although the Meanshift
search is based on the previous frame, yielding a model of the target area algorithm achieves better tracking results, it still cannot perform adap-
as follows: tive tracking for changes in the target scale. As a result, the Camshift
p
u(y)=C∑n k(⃦ ⃦ ⃦y(cid:0) hx i⃦ ⃦ ⃦2)
δ[b(x i)(cid:0) u] (4)
a mlg eo nr
t
it oh nm
M
h ea as
n
b se he ifn
t
p br yo p ao ds de id
n
g( H as i sa
c
ae lt
e
a al. d, a2 p0 t1 io6 n) , mw eh ci hc ah
n
i is
s
man ti om ip t.r o Tv he e-
i=1 Camshift algorithm can automatically adjust the scale of the tracking
frame according to the size of the target, which effectively solves the
where y is the center of the window and h is the width of the nuclear
problem of target distortion and occlusion. Such methods are widely
window.
used in practice due to their fast convergence nature, but the slow
Step 3: Similarity judgment: The similarity between the target tem-
tracking speed has not been fundamentally addressed.
plate and the moving target in the scene is measured according to the
Bhattacharyya distance, with the Bhattacharyya coefficient defined as
3.2.4. Correlation filter
follows:
This section mainly describes the correlation filtering algorithms
ρ(p,q)=∑m √̅ p̅̅ u̅̅ q̅̅ u̅̅
(5)
using artificial features, (see Section 4.2 for the correlation filtering
u=1 tracking algorithm based on depth features) introduces their advantages
and disadvantages in detail, and gives the performance of the algorithm
Step 4: Performing process matching: Finding the maximum value of
in Table 2. Correlation filtering is mainly used to determine the corre-
the similar probability function and calculating the new position of the
lation of two signals, which is calculated by convolving the two signals.
target.
The higher the value obtained, the more similar the two signals are. In
Step 5: When the similarity between the target model and the
2010, Bolme et al. (2010) applied correlation filtering to target tracking
tracking model is less than a specific threshold, the iteration stops and
for the first time. It essentially trains the filter based on the first frame
the target area to be tracked is obtained.
target sample. Then, the filter is used to search the area where the target
The traditional Meanshift algorithm has several advantages for fish
is located, the target position is determined according to the response
tracking:
value, and the filter is continuously updated during the tracking process
(Fig. 8).
(i) The algorithm is not very computationally intensive and allows
The core idea of the correlation filtering algorithm is to use a mini-
real-time tracking of fish when the target area is known.
mum output sum of squared error (MOSSE) filter to train images to
(ii) It uses a kernel function histogram model and is insensitive to fish
minimize the sum of squared errors. Then, the appearance of the tracked
edge occlusion, target rotation, distortion and background
target is modeled (Bolme et al., 2010). The processing flow of the al-
motion.
gorithm is as follows:
Step 1: First train the correlation filter to minimize the sum-of-
At the same time, the Meanshift algorithm also has the following
squares error between the actual output FiH* and the desired outputGi.
shortcomings: ∑
min |F i⊙H*(cid:0) G i|2 (6)
H
(i) The algorithm lacks the necessary template updates. i
(ii) Since the window width size remains constant during tracking, Step 2: Then use the trained correlation filter H* to correlate with the
tracking fails when the target scale changes. input image F to find its responseG:
In response to the shortcomings of the Meanshift algorithm and the G=F i⊙H* (7)
apparent limitation that machine fish are susceptible to water wave Step 3: Finally, the PSR is used as a measure of the peak intensity of
fluctuations in target tracking. Xin and Wei (2015) proposed an the response. The location of the new target will be followed only if the
Table 2
Representative work on correlation filtering tracking algorithms. DP: distance precision; OS: overlap success; CLE: center location error (in pixels); OP: mean overlap
precision; ACC: Accuracy; ROB: Robustness; EAO: expected average overlap.
Reference Approach Features Journals Dataset Performance Description
Bolme et al., 2010 MOSSE Raw pixel CVPR – PRE: 35.7 %; FPS:669 Introducing correlation filtering to the field of target
tracking
Henriques et al., KCF HOG TPAMI the 50 Videos DP:73.2 %; FPS: 172 HOG features were introduced instead of the original
2015 Dataset features.
Ma et al., 2015 HCF CNN ICCV refer KCF DP: 89.1 %; OS: 74.0 %; CLE: Introducing deep features into KCF
15.7; FPS:11.0
Danelljan et al., SRDCF HOG ICCV OTB2013; OP13:78.1 %; OP15:72.9 %; Better resolution of edge effects and improved
2015 OTB2015 FPS: 4 tracking quality
Danelljan et al., DeepSRDCF CNN, HOG ICCV OTB2013 OP: 79.4 %; DP:84.9 %；FPS: Indicate that tracking questions do not require too
2016a 0.2 much semantic information
Galoogahi et al., BACF HOG ICCV VOT2015 ACC: 59 %; ROB: 1.56； To solve the problem of target background changing
2017 FPS:26.7 over time
Li et al., 2018a STRCF HOG, CN, CVPR VOT2016 ACC: 53 %; ROB: 1.32; FPS: 30 Introducing temporal regularization into a single
Grayscale sample SRDCF Algorithm
Li et al., 2018a DeepSTRCF CNN, HOG CVPR VOT2016 ACC: 55 %; ROB: 0.92; FPS: Introducing deep features into STRCF
24.3
Danelljan et al., C-COT CNN ECCV VOT2015 ACC: 54 %; ROB: 0.82; FPS: 1 Generalizing the learned detection process to the
2016b continuous spatial domain
Zolfaghari et al., ECO CNN, HOG, CN CVPR VOT2016 ACC: 55 %; ROB: 0.20; EAO: Group samples to solve overfitting problem, speed is
2018 37.5 %; FPS: 8 improved
7

# Page 8

Y. Mei et al. C o m p u t e r s a n d E l e c t r o n ic s i n A g r i c u l t u r e 201(2022)107335
Fig. 8. Frame diagram of correlation filtering tracking algorithm.
PSR is greater than a certain threshold, otherwise, step 1 is executed. background of the tracked target over time. The accuracy of BACF is 53
Lopez-Marcano et al. (2021) employed MOSSE, Seq-NMS and %, the robustness is 1.56, and the speed reaches 26.7 frames/s on the
SiamMask algorithms to track fish movement and evaluated their ac- VOT2015 dataset. The tracking methods summarized above are all
curacy in characterizing movement. The MOSSE algorithm uses the methods that use artificial features. They can update the model in time
Fourier transform operation, which greatly improves the operation to adapt to changes in the target. This kind of algorithm has low
speed and makes the algorithm have good real-time performance. computational complexity and improves the real-time performance of
However, since the scale changes are not considered, the robustness of target tracking.
the algorithm is relatively poor. To solve these problems, Henriques
et al. (2015) proposed the kernel correlation filter (KCF) algorithm. It 4. Fish tracking algorithm using deep learning
uses features to replace the original pixels used in MOSSE, which en-
hances the filter’s ability to discriminate between targets and environ- In recent years, deep learning technology is widely used in the field
ments. The KCF algorithm compensates for the lost target and the of target tracking, which not only improves the detection performance of
occlusion in the tracking process. It effectively reduces the errors caused targets, but also greatly promotes the development of fish detection, and
by illumination, occlusion and water surface fluctuation, and achieves lays a good foundation for the research of fish tracking. We divide
accurate and fast tracking (Zou et al., 2021). To judge whether the water tracking algorithms using deep learning into the following categories.
quality is normal by the motion characteristics of the fish, Cheng et al.
(2019) used two cameras to film the fish and used the Kuhn-Munkres 4.1. Tracking-by-detection
(KM) algorithm to match the target points of the fish body. It uses a
Kalman filter to update the current state and find the optimal tracking To solve the tracking problem of moving objects, many different
position as the tracking result. The authors compensate for the tracking types of methods have emerged. For example, the tracking-by-detection
process with the KCF algorithm, which allows them to obtain the target’s method uses the tracking algorithm to learn the temporal information of
motion trajectory directly, avoiding the need to re-extract the center-of- target changes in the video sequence, and the detection algorithm to
mass points from the image sequence and greatly improving efficiency. learn the spatial information of the target in a single frame image. After
However, its tracking model only uses HOG features, which can easily that, the two are organically combined to improve the performance of
lead to tracking failure when the feature information is blurred. More- video target detection (Kang et al., 2016). Convolutional neural net-
over, the learning rate is fixed, making the tracking model vulnerable to works (CNN) play an important role in target detection, which was first
contamination from the surrounding environment and unsuitable for proposed by Lecun (1989). The basic structure of the CNN consists of an
long-term tracking. input layer, convolutional layer, pooling layer, fully connected layer and
In the tracking algorithm based on correlation filtering, the solution output layer, as shown in Fig. 9. In 2012, Krizhevsky et al. (2012) pro-
of the objective function needs to be converted to the frequency domain posed the AlexNet network model and won the ImageNet image classi-
by Fourier transform. However, in this transformation process, the fication competition. As a result, CNN is successfully introduced into the
image windows need to be spliced cyclically. The stitched image will field of computer vision. Since then, many classical convolution network
produce discontinuities at the edges, which will lead to edge effects and models have emerged, such as VGGNet, GoogLeNet and ResNet (Sapi-
affect the tracking effect of the target. To solve the edge effect, Danelljan jaszko and Mikhael, 2018).
et al. (2015) proposed the Spatial Regular Correlation Filter (SRDCF) CNNs are often used to study the behavioral states of fish (Ben Tamou
algorithm. The algorithm introduces a spatial regularization component et al., 2021; Xu and Cheng, 2017; Nair and Domnic, 2022). For non-rigid
and uses the regularization weight to penalize the filter coefficients in fish with similar appearance and frequent mutual occlusion, Wang et al.
the training process, thereby generating a more discriminative model. (2017c) implemented fish head detection using CNN. And by identifying
SRDCF model is built on multiple training images, which further in- the head image of each fish in each frame to correlate data across frames,
creases the difficulty of improving efficiency. Therefore, Li et al. (2018a) a large number of fish can be tracked reliably over time. When dealing
proposed a spatio-temporal regularized correlation filter (STRCF) by with fish detection problems, according to the detection steps, the
introducing time regularization into a single sample SRDCF. It can convolutional neural network model can be divided into one-stage and
handle boundary effects without much loss of efficiency and out- two-stage. Two-stage divides fish detection into two stages, firstly
performs SRDCF in terms of accuracy and speed. The accuracy of STRCF generating region proposals for fish and then classifying the candidate
is 53 %, the robustness is 1.32, and the speed reaches 30 frames/s on the regions (also correcting for location) (Jager et al., 2017). This type of
VOT2016 dataset (Table 2). Since the previous correlation filtering al- algorithm needs to run the detection and classification process several
gorithm only models the target, the change of target background with times, therefore, the accuracy of this type of algorithm is high, and the
time is ignored. To solve this problem, Galoogahi et al. (2017) proposed detection speed is slow. Representative models are R-CNN, Fast R-CNN,
a background-aware correlation filtering (BACF) algorithm. The algo- SPP-Net, etc.
rithm uses the HOG feature to dynamically model the foreground and Due to the low efficiency of the candidate region detection model,
8

# Page 9

Y. Mei et al. C o m p u t e r s a n d E l e c t r o n ic s i n A g r i c u l t u r e 201(2022)107335
Fig. 9. CNN network structure diagram.
Redmon and Farhadi (2016) proposed the YOLO algorithm. The idea is one after another. In addition, One-stage network models include SSD,
to train a single neural network directly on the whole input image as RSSD, DSSD, etc. The above algorithm can be used to solve the problem
input, using a form of grid prediction instead of generating a network of of poor tracking due to fast motion and occlusion. Barreiros et al. (2021)
candidate regions. It does not require complex operations and greatly utilized the target recognition convolutional network YOLOv2 to
improves the detection speed of the network. As shown in Fig. 10, the segment fish head regions to optimize the detection of individual fish. In
structure of YOLO contains a total of 24 convolutional layers and 2 fully the tracking stage, Kalman filtering is used to estimate the optimal state
connected layers. The algorithm continues the core idea of GoogleNet of the fish head position in each frame, and then the trajectories of each
and truly implements an end-to-end target detection algorithm. In 2017, fish are connected between frames.
Redmon et al. proposed the YOLOv2 algorithm based on the YOLO al-
gorithm (Redmon and Farhadi, 2016). It improved the original feature
4.2. Depth features combined with correlation filtering
extraction network of YOLO by adding batch normalization after each
convolutional layer and multi-scale training. It also added K-mean
Good features are a prerequisite for good tracking, and deep neural
dimensional clustering, which led to another improvement in detection
networks can learn rich representations and extract complex and ab-
speed and accuracy. However, the detection and recall probability
stract features from them. Their extracted deep features are robust,
problems for small targets are not well improved. In 2018, Redmon and
descriptive and more accurate than traditional manual features (Xiao
Farhadi (2018) proposed the YOLOv3 model based on YOLOv2, which
et al., 2020). On the other hand, the application of correlation filtering
uses Darknet-53′s network for feature extraction. To improve the
methods has led to a substantial increase in the speed of object tracking.
detection accuracy of small targets, YOLOv3 borrows the idea of multi-
To improve the overall performance of tracking algorithms, people have
layer feature fusion, where deep feature maps are up-sampling and
started to introduce deep learning into correlation filtering. In Table 2,
stacked with shallow feature maps for feature fusion, and each candidate
we describe the correlation filtering algorithms using depth features,
frame can predict multiple classifications. Then, YOLOv4 (Bochkovskiy
and list their accuracy, speed and other performance.
et al., 2020) and YOLOv5 (Yao et al., 2021) network models appeared
The general idea of the depth feature combined with the correlation
Fig. 10. YOLO typical network structure.
9

# Page 10

Y. Mei et al. C o m p u t e r s a n d E l e c t r o n ic s i n A g r i c u l t u r e 201(2022)107335
filtering algorithm is to use an off-the-shelf neural network model to summarized in Table 2, and each method is reviewed.
provide depth features for the correlation filtering tracking algorithm.
The accuracy and robustness of the correlation filtering algorithm using
4.3. End-to-end tracking method
depth features are significantly improved compared to the correlation
filtering algorithm using manual features. For example, compared with
The deep learning tracker (DLT) algorithm learns generic image
the KCF tracking algorithm, the hierarchical convolutional features
features from large image datasets as auxiliary data by using stacked
(HCF) algorithm (Ma et al., 2015) replaces the HOG features with hi-
denoising autoencoders (SDAE). The learned features are then trans-
erarchical convolutional features, which uses the network framework of
ferred to online tracking tasks, successfully applying deep learning to
VGG-19, and the network is trained on ImageNet. The algorithm uses the
object tracking (Wang and Yeung, 2013). As a result, the efficiency of
output of conv3-4, conv4-4 and conv5-4 as the feature extraction layer,
DLT is significantly improved, making it more suitable for real-time
and the extracted features are learned by correlation filters to obtain
tracking. In the literature (Lai et al., 2019), the authors propose a 3D
different templates. The three confidence maps obtained are then
version of a convolutional network of trackers (CNT) for underwater fish
weighted and fused to obtain the final target location. The distance
multi-target tracking. It features the extraction of spatio-temporal fea-
precision of KCF is 73.2 %, and the precision of HCF is improved to 89.1
tures between successive frames, making the fish target template more
%. However, due to the introduction of the depth feature, the speed
robust in tracking. The method does not require pre-training and has
decreased from 172 fps to 11 fps. In addition, the DeepSRDCF algorithm
achieved good results. Rather than the above methods, Nam and Han
(Danelljan et al., 2015) greatly improves the tracking performance by
(2016) proposed a new idea by training a multi-domain learning
replacing the hand-crafted features with CNN features on basis of
network structure (Multi-Domain Network, MDNet) (Fig. 12). Capable
SRDCF. It also illustrates that CNN features work better in solving the
of separating multiple target-independent information from the target,
problem of tracking by taking the underlying features, which do not
the model can be well applied to the task of target tracking, enabling
require too much semantic information. On the OTB2013 dataset,
end-to-end tracking. Konovalov et al. (2019) investigated the problem of
compared with the SRDCF algorithm, the mean overlap precision of the
underwater fish target detection with weak multi-domain supervision
DeepSRDCF algorithm increased from 78.1 % to 79.4 %, but the speed
and achieved good results.
decreased from 4fps to 0.2fps. Similarly, the DeepSTRCF algorithm (Li
et al., 2018a) combines the output of the conv3 layer of the VGGM
network with HOG and CN features for STRCF training. In Table 2, we 4.4. Tracking method based on Siamese network
use accuracy, robustness and speed as performance indicators to
compare the performance of STRCF and DeepSTRCF on the VOT2016 This section introduces the Siamese series of target tracking algo-
dataset. The accuracy of DeepSTRCF is 55 %, which is 2 % higher than rithms, and compares the accuracy, robustness and speed of each algo-
STRCF. However, its robustness dropped from 1.32 to 0.92, and its speed rithm. The characteristics of some adopted Siamese network tracking
dropped from 30fps to 24.3fps. On the other hand, the continuous algorithms are described in Table 3, including their Backbone, Journals,
convolution operators for visual tracking (C-COT) (Danelljan et al., Output, Scale estimation, and Speed (fps). In addition, we also comment
2016b) is another breakthrough in correlation filtering algorithm after on these algorithms. In Table 4, we give the specific performance
KCF. Compared with the KCF algorithm, it uses the deep neural network comparison of the tracking algorithm based on the Siamese network on
VGG-net to extract features. The cubic spline function is used for GOT-10 k, VOT2018 and OTB2015. The characteristics and performance
interpolation, and the feature maps of different resolutions are extended of each method are described in Table 5.
to the continuous space domain of the same period through interpola- To address the lack of data and poor real-time performance of deep
tion operation. Then Hessian matrix can be used to obtain the sub-pixel learning in the field of target tracking, Bertinetto et al. (2016) proposed
precision of the target position. On this basis, the Efficient Convolution the Siamese network framework. It uses a convolutional network to
Operator for Tracking (ECO) (Zolfaghari et al., 2018) improves the C- extract features from the target template and search area, and then
COT algorithm for visual tracking from three aspects: filter selection, performs the relevant operations to generate a response map. The peak
sample set and model update strategy. It realizes the fusion of traditional points on the response map are the locations where the targets are
artificial and convolutional features, which improves the running speed located (Fig. 13). The SiamFC algorithm uses a simple AlexNet network
of the algorithm (Fig. 11). All of the above methods have good tracking for feature extraction. Its network has only 5 convolutional layers, no
performance and are promising for application in fish tracking. The padding operation is added, and each convolutional layer is followed by
specific performance of the correlation filtering algorithms is a ReLU layer. The algorithm simplifies the process of calculating simi-
larity and greatl improves the tracking speed. The algorithm simplifies
Fig. 11. Architecture overview of ECO.
10

# Page 11

Y. Mei et al. C o m p u t e r s a n d E l e c t r o n ic s i n A g r i c u l t u r e 201(2022)107335
Fig. 12. multi-domain network structure diagram.
Table 3
Summary of tracking algorithms based on the Siamese Network.
Method Backbone Journals Output Scale estimation Speed (fps) Comment
SiamFC AlexNet ECCV Response map Patch-pyramid 58 Simple structure and real-time, but less robust to scale changes
SiamRPN AlexNet CVPR Response map Anchor 160 Effectively reduces the impact of changes in target scale on tracking results
DaSiamRPN AlexNet ECCV Response map Anchor 160 Improved generalization and discriminatory ability of the tracker
SiamRPN++ ResNet-50 CVPR Refer SiamRPN Refer SiamRPN 35 Enables more accurate tracking results
SiamFC++ GoogleNet AAAI Refer SiamFC Refer SiamFC 90 Significant improvements in tracking efficiency
Table 4
The specific performance comparison of the tracking algorithm based on the Siamese network on GOT-10 k, VOT2018 and OTB2015. SR: Success Rate; AO: Average
Overlap Rate; A: Accuracy; R: Robustness; EAO: Expected Average Overlap; S: Success; P: Precision.
Method GOT-SR0.5 GOT-SR0.75 GOT-AO VOT2018-A VOT2018-R VOT2018-EAO OTB2015-S OTB2015-P
SiamFC 35.3 9.8 34.8 0.503 0.585 0.188 0.582 0.772
SiamRPN 58.1 27.0 48.3 0.586 0.276 0.383 0.637 0.851
DaSiamRPN – – – 0.569 0.337 0.326 0.658 0.880
SiamRPN++ 61.8 32.5 51.8 0.600 0.234 0.414 0.696 0.914
SiamFC++ 69.5 47.9 59.5 0.587 0.183 0.426 0.683 –
Table 5
Representative work of different types of tracking algorithms. ARI: Adjusted Rand Index. AMI: Adjusted Mutual Information.
Reference Approach Dataset Category Performance Comment
Shantaiya et al., Kalman filter MITTrafficvideo Traditional ACC: 85 % Relatively simple, suitable for tracking fish in simple scenes. However,
2015 tracking failed when the fish exhibited irregular movements
Breitenstein Particle filter ETHZ Central Traditional ACC: 72.9 %; PRE:70.0 Handles the non-linear, non-Gaussian case in fish tracking, compensating
et al., 2011 % for the small range of applicability of the Kalman filter
Jang and Jiang, Meanshift Lupus Traditional ARI: 0.1399; AMI: Not computationally intensive, it handles edge occlusion, object rotation,
2021 0.2042; Runtime: 3.82 distortion, and background motion well. However, tracking may fail when
s the target scale changes
Galoogahi et al., Correlation VOT2015 Traditional ACC: 59 %; ROB: 1.56 Fast and accurate; improvements focus on five areas: features, scaling,
2017 filter boundary effects, target chunking, and response adaptation
Xu and Cheng, Tracking-by- Zebrafish video Deep PRE:98.31 %; Consider tracking as a foreground (target) and background classification
2017 detection Learning REC:99.54 % FM: problem.
98.92 %
Wang and End-to-end Animal Deep ACC:87.3 %; CLE: 10.2 This is mainly achieved using deep learning, but the method is not very fast.
Yeung, 2013 Tracking Learning There is no great improvement in effectiveness compared to traditional
methods, and at this stage little has been landed.
Li et al., 2019 Siamese VOT2018 Deep ACC: 0.503; ROB: Mainly tracks a single target fish; simple structure and real-time
network SiamFC Learning 0.585；EAO: 0.188
the process of calculating similarity and greatly improves the tracking scale information of the target, Li et al. proposed the SiamRPN tracking
speed, and the speed reaches 58 FPS, which meets the requirements of algorithm (Li et al., 2018b). SiamRPN abandons the traditional scale
real-time tracking. As a result, SiamFC stands out among target tracking search strategy and introduces the Region Proposal Network (RPN) (Ren
algorithms that are based on correlation filtering. But its accuracy on the et al., 2017). The RPN contains two branches, one for foreground and
VOT2018 dataset is only 0.503, and its performance needs to be further background classification and the other for bounding box regression. By
improved. fusing the two results, the current position and size of the tracking target
Considering that the regression of SiamFC to the target scale still can be obtained at the same time. The anchor mechanism of RPN
adopts the traditional scaling form and cannot accurately obtain the effectively reduces the influence of target scale changes on the tracking
11

# Page 12

Y. Mei et al. C o m p u t e r s a n d E l e c t r o n ic s i n A g r i c u l t u r e 201(2022)107335
Fig. 13. SiamFC tracking algorithm framework.
results. The algorithm can reach 160 FPS, which is much faster than the Previous tracking methods have proposed various target state esti-
SiamFC algorithm in terms of speed. It has an accuracy of 0.586 on the mation methods, but seldom consider the characteristics of the visual
VOT2018 dataset, which is slightly higher than the SiamFC algorithm. tracking problem itself. Xu et al. (2020b) proposed the SiamFC++al-
However, due to the relatively small number of datasets used in the gorithm based on the framework of SiamFC and considering the char-
training phase, the generalization performance of SiamRPN for the acteristics of the tracking problem itself. The algorithm also introduces
model is weak, and it still has a high response when the target is lost. classification and target state estimation branches, unambiguous clas-
Although the above algorithms, such as SiamFC and SiamRPN, strike sification score and evaluation quality score branches, which greatly
a balance between accuracy and speed, there are still some issues that improves the tracking performance on the original basis. Particularly, on
need to be addressed. On the one hand, the above algorithms can only the large-scale TrackingNet dataset, SiamFC++achieves a pre viously
distinguish the foreground from the non-semantic background, and unseen AUC score of 75.4 while running at over 90 FPS, which is far
when the background is cluttered, the tracker performance will deteri- above the real-time requirement.
orate. On the other hand, although they achieved a huge improvement In general, the algorithm based on the Siamese network has become
in speed, the model cannot be updated online. Most of them adopt a the current mainstream tracking algorithm. The initial Siamese network
local search strategy, when the tracking target is completely occluded, is far faster than real-time, but its accuracy is not as good as related
the tracking will fail. For the shortcomings of the above algorithm, Zhu methods that combine deep features. With the deepening of research,
et al. proposed the DaSiamRPN (Zhu et al., 2018) algorithm. Compared researchers continue to improve the Siamese network algorithm in terms
with the SiamRPN, the algorithm is improved in 3 parts. of multi-scale detection, training sample sets, search strategies, and
strict translation invariance. And a deeper network structure is applied
(i) The datasets ImageNet Detection and COCO Detection are in the Siamese network, which has surpassed the tracking algorithm of
introduced in the model training phase, which increases the correlation filtering combined with deep features in terms of accuracy
number of positive samples. and speed. Although the tracking method based on the Siamese network
(ii) It uses different kinds of positive samples and negative samples has made breakthrough progress, most of the algorithms adopt offline
containing targets (non-targets) for training, eliminating the training. Therefore, it is crucial to explore the online training method of
tracking inaccuracy problem caused by sample imbalance. this algorithm in the future.
(iii) A local-to-global search strategy is proposed to improve the
performance of long-term tracking. 5. Target tracking dataset and evaluation metrics
DaSiamRPN enhances the discriminative ability of the classifier and 5.1. Target tracking dataset
improves the generalization performance of the model. It can better
handle the occlusion problem and improve the performance of the al- Tracking datasets are an important part of the target tracking tasks. It
gorithm for long-term tracking. The algorithm speed reaches 160FPS, provides data support for model training and algorithm verification. At
which meets the requirements of real-time tracking. present, there are many common datasets in the field of target tracking,
The above methods all use AlexNet as the feature extraction network such as the OTB, VOT, LaSOT, and GOT-10 k datasets. We experiment
and do not use a deeper and more powerful feature extraction network. with different types of algorithms on the OTB2015 dataset, and the re-
To gain improvements in tracking accuracy, Li et al. (2019) analyzed sults are shown in Table 6.
existing Siamese trackers, proving that the core reason is the lack of The different types of tracking methods such as correlation filtering
strict translation invariance. Then, they propose the SiamRPN++ al- and deep learning were compared on the OTB-2015 dataset (Table 6). It
gorithm, which proposes a simple and effective sampling strategy that can be found that the accuracy and success rate of the deep learning
breaks the space invariance limit. Additionally, the algorithm introduces methods are higher than the correlation filtering type methods. Deep
a deeper backbone network and uses deep cross-correlation operations learning methods extract features with high robustness, so the trained
to solve asymmetric problems. For the first time, the algorithm surpasses models are more perfect. The speed of correlation filtering algorithms
the correlation filtering methods in accuracy, and reaches 35FPS in using depth features is mostly within 30 FPS, which is not sufficient for
speed, which still meets the real-time requirements. It achieves good real-time tracking of targets. In recent years, Siamese network tracking
results on multi-target tracking datasets. In the study of fish, Siamese methods have developed rapidly. The early SiamFC series tracking al-
network algorithms play an important role. Wang et al. (2022) used the gorithms represented by SiamFC are much faster than real-time. But the
SiamRPN++ algorithm to achieve multi-objective tracking of anoma- accuracy is not as good as the correlation filtering method combined
lous fish and achieved better results. with deep features (Table 3, Table 4). With the continuous improvement
12

# Page 13

Y. Mei et al. C o m p u t e r s a n d E l e c t r o n ic s i n A g r i c u l t u r e 201(2022)107335
Table 6
Performance of different types of tracking algorithms on OTB2015.
Algorithm index KCF SRDCF DeepSRDCF CCOT ECO MDNet SiamFC SiamRPN++
Precidion 0.765 0.791 0.846 0.884 0.899 0.895 0.772 0.903
Success 0.544 0.587 0.629 0.672 0.681 0.675 0.581 0.687
of the Siamese network by researchers, its accuracy and speed have 5.2. Evaluation metrics
surpassed the correlation filter tracking algorithm combined with deep
features. It can be seen that the Siamese network tracking algorithm has The evaluation indexes mainly used by target tracking algorithms
become the mainstream algorithm in the tracking field, and it is also the usually include Center Location Error (CLE) and Overlap Score (OS)
trend of future development. (Marvasti-Zadeh et al., 2022). According to the above two basic pa-
In fish research, Fish4-Knowledge, 3D-ZeF, LCF-14, LCF-15, Sea- rameters, the evaluation indexes of accuracy and robustness of the al-
CLEF2016 and DeepFish datasets can be used as tracking datasets. gorithm are introduced below.
Table 7 presents information such as the number of videos or images,
resolution, number of labeled fish, and fish species in the fish tracking 5.2.1. Center location error
dataset. (i) Center location error: CLE is the Euclidean distance between the
In Table 7, all datasets are videos about fish. Among them, the Fish4- predicted frame center position (xlr,ylr) of each frame in the video
Knowledge dataset contains about 700,000 10-minute underwater video sequence and the corresponding ground truth center position (xgt,
clips in recent years. The video shows several phenomena from sunrise ygt)(Fig. 14(a)). Usually, the average value of the sum of the positioning
to sunset, such as turbid water and algae on the lens. At the same time, it errors of all frames is taken as the evaluation index. Among them, the
contains more than 3000 different fish species. 3D-ZeF (Pedersen et al., center position error in a certain frame is shown in Equation (8).
2020) is a dataset for multi-target zebrafish tracking in stereoscopic 3D √̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅
RGB. It consists of eight sequences with a duration between 15 and 120 s CLE= (x lr(cid:0) x gt)2+(y lr(cid:0) y gt)2 (8)
and 1–10 free moving zebrafish. The videos have been annotated with a
total of 86,400 points and bounding boxes. Dataset is download at https: CLE is an older metric that is sensitive to dataset annotation and does
//vap.aau.dk/3d-zef. LCF-14 is a smaller dataset containing 1000 videos not account for tracking failures. However, when the tracker loses the
of more than 10 species of fish. LCF-14 dataset is publicly available at target, the predicted tracking position is random, and the average error
https://www.imageclef.org/2014/lifeclef/fish. The LCF-15 dataset value may not be able to accurately evaluate the performance of the
consists of 93 underwater videos of 15 species of fish. It has more tracker. Therefore, on the OTB dataset (Xu et al., 2018), the precision
ambient noise and poorer lighting than the LCF-14. The datasets are when the positioning error threshold is 20 pixels is taken as the final
accessible online at http://www.imageclef.org/lifeclef/2015/fish. In accuracy of the algorithm.
the SeaCLEF2016 dataset, the training set contains 20 videos and more (ii) Distance precision (DP): DP is achieved by computing the CLE. It
than 20,000 sample images. The main challenge of this dataset is the represents the percentage of video frames whose CLE is less than a given
variation of illumination. At the same time, in order to better track fish, threshold to the total video frames. The details are as follows:
Jager et al. (2017) has added ground truth track annotation. The opened N
DP= CLE⩽T0 (9)
dataset is download at https://www.imageclef.org/lifeclef/2016/sea. N
The total number of video frames captured in the DeepFish dataset is
39,766 frames, which are captured by cameras mounted on metal
Where N is the total number of video frames, NCLE⩽T0 is the total
number of video frames whose center positioning error is less than the
frames. Compared to current fish datasets, it contains a large number of
complex scenes of fish habitats. Dataset is download at https://github.co
given threshold, and T0 is the given threshold.
(iii) Precision plot: The precision plot is composed of the percentage
m/alzayats/DeepFish.
of the number of frames when the centering error is less than different
thresholds. Since different thresholds yield different percentages, the
precision plot can be obtained by adjusting the thresholds. This method
Table 7
reflects the positional accuracy of the tracked target by the central
Overview of various datasets.
localization error, but does not reflect the change of target scale and size.
Dataset Number of videos Resolution Number of Species
labeled
5.2.2. Overlap score
fish
(i) overlap score (OS): Because the center position error cannot
Fish4- 700,000 videos with 10 320 ×240 –– 3000
Knowledge min each clip pix
3D-ZeF 8 video sequences with 2704 × 86,400 1
a duration between 15 1520 pix
and 120 s and 1–10 free
moving zebrafish
LCF-14 1000 videos 640 ×480 19,868 10
pix
320 ×240
pix
LCF-15 93 videos 640 ×480 9000 15
pix
320 ×240
pix
SeaCLEF2016 Training set consisting 640 ×480 9000 15
20 videos and 20,000 pix
images sample. 73 test 320 ×240
videos pix
DeepFish 39,766 video frames 1920 × 3200 ––
1080 pix
Fig. 14. Evaluation parameters.
13

# Page 14

Y. Mei et al. C o m p u t e r s a n d E l e c t r o n ic s i n A g r i c u l t u r e 201(2022)107335
evaluate the scale change of the target during the tracking process, the occlusion and morphological changes in the process of feeding. In terms
researchers propose an evaluation index based on the area overlap ratio. of disease diagnosis: the morphology of diseased fish usually changes.
It is the Intersection over Union (IOU) of the predicted bounding box For example, Turning over arises mainly because of fish diseases, so this
area Rlr and the corresponding ground truth areaRgt. The overlap score behavior often appears individually from time to time, making it hard to
in a certain frame is shown in Equation (10). be noticed. Once these abnormal reactions are not found in time, it is
⃒ ⃒ very likely to cause large number of fish death. The diseased fish can be
OS=IOU=⃒ ⃒ ⃒R Rl lr r∩ ∪R Rg gt t⃒ ⃒ ⃒ (10) tracked using a detection-based tracking algorithm (Section 4.1), which
finds the diseased fish by a target detection algorithm and then tracks it
(ii) overlap precision (OP): The OP is implemented by computing the using a tracking algorithm. (iii) In terms of fish counting: it mainly faces
OS. It represents the percentage of video frames (NOS⩾T1) with overlap challenges such as occlusion and image blur. Deep learning methods
score (OS) greater than a given threshold (T1) out of all frames (N) of the (Section 4) can automatically extract low-level and high-level features
video. The specific calculation method is as follows: from large-sample blurred images to identify subtle features of fish.
Then, the Kalman filter algorithm (Section 3.2.1) is used to predict the
N
OP= OS⩾T1×100% (11) fish location, which can effectively solve the obscuration problem that
N
occurs during the fish counting process and achieve accurate fish
(iii) Success plot: The success plot is composed of the percentage of counting.
the number of frames for which the overlap score is greater than a
threshold (between 0 and 1). Because the percentages obtained are 6.1. Potential applications in precision feeding
different for different thresholds, a success plot can be obtained by
adjusting the thresholds. The success rate at an overlap threshold of 0.5 In aquaculture, accurate feeding needs to be based on the actual
is generally used as the final success rate of the algorithm. In addition, feeding needs of fish, and feeding needs to be carried out at an appro-
the success rate can also be calculated from the area (Area Under Curve, priate amount at an appropriate time to meet the necessary conditions
AUC) enclosed by the success rate curve and the coordinate axis. The for the healthy growth of fish. However, feeding fish is much more
method evaluates the tracking accuracy by predicting the overlap ratio problematic than feeding livestock. Over 60 % of feed in aquaculture
between the target frame and the ground-truth frame to reflect changes systems is reported to be in the form of tiny particles (Masser, 1992), the
in target scale and size. breakdown of which consumes oxygen and produces ammonia and other
In addition, there are many parameters to evaluate the performance toxic substances. As the effectiveness of feeding control methods directly
of the algorithm. For example, accuracy represents the average overlap affects feed conversion rates and reproduction, determining when to
between the predicted and ground truth of the algorithm. Robustness start and stop feeding is important to improve fish welfare and reduce
represents the number of tracking failures during the tracking process of costs (Føre et al., 2011; Wu et al., 2015). Until now, fish feeding has been
the algorithm (a tracking failure is considered when the overlap score is mainly based on manual identification, a method often influenced by the
0). Expected Average Overlap（EAO) is used to measure the accuracy individual experience of the observer and unable to be quantified using
and robustness of the algorithm as a whole. The speed of the tracking uniform criteria (Liu et al., 2014). Apart from that, artificial fish rearing
algorithm is expressed as FPS. and management are costly (Verdal et al., 2018), with low labor pro-
ductivity, high environmental stress, high reproductive risk and the
5.2.3. Robustness inability to adapt rearing strategies to the specific conditions of the fish
Since many tracking algorithms are sensitive to initialization, stock (Edwards, 2015). The continuing increase in labor costs and an
robustness measures are proposed. Specifically, there are two kinds of aging workforce are exacerbating the problem of inefficient fisheries
robustness metrics. The first is Temporal Robustness Evaluation (TRE), production, making research into intelligent aquaculture feeding control
which refers to evaluating the performance of the algorithm by selecting methods adapted to the needs of fish of great importance (Zhou et al.,
different frames as the starting frame for initialization. In contrast, 2018b).
Spatial Robustness Evaluation (SRE) is computed by perturbing the In recent years, there has been increasing interest in intelligent
initialization from different positions in the first frame. Therefore, this is feeding control based on changes in fish behavior and growth status
also the origin of the SRE name. (Zhou et al., 2018b). Studies have shown that the swimming speed and
direction of fish change during feeding so that changes in feeding
6. Applications of tracking method in fish research behavior reflect appetite (Zhao et al., 2016). Fish tracking technology
using machine vision is to accurately analyze the feeding behavior of
The aquaculture industry is currently experiencing a gradual shift fish by detecting and tracking each individual in the group, and then
from the traditional crude farming model to a modern intensive, precise extracting characteristic parameters from the established movement
and digital farming model (Yue and Shen, 2022). The study of fish trajectory. Therefore, the analytical results of fish feeding behavior
tracking techniques has an important role in the development of fine depend on the accuracy of detection and tracking. Currently, many
farming. The use of fish tracking techniques provides a better under- studies focus on fish feeding activities in controlled environments.
standing of fish behavior and is important in the areas of precision However, in real aquaculture environments, target tracking loss may
feeding, disease diagnosis, counting and parental tracking of fish. (i) In occur due to fish occlusion, overlap and complex movements. Therefore,
terms of accurate feeding: there will be occlusion and morphological methods suitable for fish tracking are crucial for studying fish feeding.
changes in the process of feeding. The interframe difference method Qian et al. (2016) proposed a multi-fish tracking method based on fish
(Section 3.1.1) and background modeling method (Section 3.1.2) can be head detection, which uses the shape and grey-scale features of fish head
adopted to segment fish and analyze their feeding behavior by taking the images to determine their positions. The results show that the method
whole fish school as the research object. Optical Flow (Section 3.1.3) can determine the movement trajectories of tens of fish in low-density
avoids foreground segmentation of images by tracking fish schools to experiments. However, the accuracy of tracking groups of moving tar-
extract behavioral parameters. The deep learning method (Section 4) gets needs to be improved (Marti-Puig et al., 2018). Papadakis et al.
classifies the intensity levels of feeding (defined as “none”, “weak”, (2012) have designed a new system based on computer vision tech-
“medium” and “strong”) by recognizing the feeding behavior of fish, niques to quantify changes in fish behavior under various stresses, which
which avoids the problems of target segmentation and low computa- can identify fish feeding or escaping based on fish-net interactions
tional efficiency of fish. (ii) In terms of accurate feeding: there will be (including checking and biting) under different conditions. Sadoul et al.
(2014) quantified the dispersal and swimming of fish by characterizing
14

# Page 15

Y. Mei et al. C o m p u t e r s a n d E l e c t r o n ic s i n A g r i c u l t u r e 201(2022)107335
their behavior through two indicators, and then analyzed the estimated counting is usually achieved by manual visual inspection, which fluc-
behavioral changes before and after feeding, providing technical sup- tuates widely and is subject to certain errors. The method of fish
port for accurate feeding. Zhou et al. (2019) used a deep learning con- detection and tracking based on machine vision is a non-invasive fry
volutional neural network approach to classify fish feeding behavior and counting method that can be effectively automated without harming the
obtain higher accuracy. In summary, the detection and tracking of fish is fish. Sharif et al. (2016) segmented fish regions in video sequences using
an important part of a fish feeding system and can be used to determine background subtraction and used a Hungarian algorithm for data asso-
the hunger status of fish and changes in their surroundings. These ciation matching after estimating the fish center. Kalman filter is used to
behavioral changes can be used to determine when and how much fish track the center position trajectory of multiple fish, and then the number
are eating and to rationalize feeding strategies. However, although of fish is estimated. Spampinato et al. (2008) used a machine vision
quantification of fish feeding behavior based on tracking technology can system to detect, track and count fish. The system consists of video
reduce labor costs and provide theoretical basis for guiding production analysis, fish detection and tracking modules. Among them, tracking is
practice. But it has not been applied in real aquaculture environment. achieved by using the CamShift algorithm. The algorithm can track
objects whose numbers may change over time and can calculate fish
6.2. Potential applications in disease diagnosis numbers under conditions such as cloudy water and low contrast.
Morais et al. (2005) used computer vision technology to study the
With the increasing level of factorization and intensification of tracking and counting of underwater fish. It adopts Bayesian Filtering
aquaculture in China, the problem of diseases arising from aquaculture Technique to obtain the characteristic information of fish and handles
has become increasingly prominent (Bondad-Reantaso et al., 2005). the problem of occlusions or large inter-frame motions. In addition, a
However, traditional methods often rely on manual inspection or per- multiple kernel tracking approach is used to associate the same targets
sonal experience to determine whether farmed aquatic organisms are in across consecutive frames for fish counting purposes. However, due to
a healthy state. This approach is often time-consuming and expensive, the diversity of fish posture, deformation of fish body shape and color
and toxins or pathogens from diseased fish can quickly contaminate similarity between fish and background, the detection performance is
entire farms (Wang et al., 2020). Therefore, real-time disease moni- greatly reduced, which leads to tracking and counting errors. To address
toring of fish in production and aquaculture becomes particularly this problem, Wang et al. (2017b) proposed a closed-loop mechanism
important. There is an urgent need for fast, accurate and inexpensive between tracking and detection. This method solves the problem of error
methods to continuously monitor fish and quantify their behavior to detection effectively and reduces the tracking error to a large extent.
detect fish with the disease early. The detection and tracking method In addition, fish tracking technology is often used to track parent
using machine vision technology can monitor the abnormal fish in real- fish. Parent fish are often some high-quality economic fish, with high-
time and improve the survival rate and economic benefits of aquacul- value characteristics. Breeding and selection of parent fish are inevi-
ture. Because aquaculture is highly intensive, bacterial and parasitic tably involved in aquaculture. Therefore, it is very important to master
diseases can spread easily and quickly, which can lead to abnormal fish the physiological state and breeding process of the parent fish. Through
behavior, such as “turning over” during movement. These phenomena, a series of tests such as salt tolerance, cold tolerance, heat tolerance and
caused by low oxygen and other conditions, are usually found in groups disease resistance, fishes with strong stress resistance were screened out.
and are relatively easy to spot. “Turning over” of fish caused by disease And to speed up the breeding process to avoid sudden or unexplained
usually occurs in isolation and is not easily noticed. In response to the death of precious fish or broodstock (Wang et al., 2020). However, at
above phenomenon, Wang et al. (2022) propose an end-to-end combi- present, it mainly relies on the naked eye to observe the behavior of fish,
natorial neural network to detect and track abnormal behavior of fish. and the cost of farming is high. The adoption of machine vision tech-
The detection algorithm transmits the initial value of the target to the nology can accurately and efficiently track the parent fish and improve
tracking algorithm, which tracks the subsequent frames. It realizes end- the efficiency of aquaculture production management. Wang et al.
to-end fish abnormal behavior detection and achieves high-speed and (2019) adopted the tracking-learning-detection (TLD) algorithm, com-
accurate tracking of abnormal behavior individuals. The author (Wang bined with color and shape features, to achieve accurate and fast
et al., 2022) improved YOLOV5s by introducing multi-level features and tracking of fish. Then the behavior of the fish was monitored and
adding feature mapping in target detection. In the target tracking part, analyzed.
the multi-target tracking of abnormal fish is realized based on the single
target tracking algorithm SiamRPN, which can accurately detect and 7. Discussion and conclusion
track the possible diseased fish in real-time. Wang et al. (2020) proposed
a real-time solution for underwater fish behavior detection using deep With the continuous deep learning research, algorithms in the field
learning techniques. It can be applied to aquaculture farms to help of visual tracking have been innovated, and fish tracking, as a difficult
prevent disease and sudden death, thereby reducing economic losses. and hot problem in the field of computer vision, has received the
Overall, the general idea of applying tracking technology to fish disease attention of many scholars. This paper reviews the research progress of
diagnosis is divided into the following steps. Firstly, it is necessary to fish behavior tracking in recent years. Based on an analysis of the
build a dataset of sick fish and healthy fish, train a suitable fish tracking extensive literature, the advantages and limitations of each method are
model, and obtain the data information of their speed, acceleration, discussed and summarized in the table. The main content of this paper is
direction, rotation angle, displacement, tail beat frequency and other to introduce fish tracking methods before deep learning, such as Kalman
indicators respectively. Then, we use the tracking algorithm to track the filtering and correlation filtering, etc. It also summarizes in detail the
fish, get the current target’s speed, turning angle and other indicator fish tracking methods using deep learning, such as tracing-by-detection
data, and compare it with the indicators of healthy fish and diseased fish methods, Siamese networks, etc. At the same time, we summarize the
obtained in the dataset. Finally, set the threshold and judge whether the datasets that can be used for fish tracking, and give evaluation metrics in
fish is in a healthy state. target tracking algorithms. Furthermore, we select several representa-
tive algorithms in the tracking domain and present their experimental
6.3. Counting questions about fish data on public datasets. In fish studies, although some algorithms have
been reviewed to solve the tracking problem, there is still a long way to
Currently, one of the tasks often involved in recirculating aquacul- go for a truly general, robust, accurate and efficient fish vision tracking
ture is counting, especially during the sale process, where the price is method. After our discussion and analysis of tracking methods, future
usually determined by the number of fish. As a result, fry counting takes research on fish tracking methods can be considered from the following
up a larger part of the task in the aquaculture process. Traditional fry aspects.
15

# Page 16

Y. Mei et al. C o m p u t e r s a n d E l e c t r o n ic s i n A g r i c u l t u r e 201(2022)107335
(1) The problem of difficult fish feature extraction. For the diffi- Barron, J.L., Fleet, D.J., Beauchemin, S.S., 1994. Performance of optical flow techniques.
culties faced in fish tracking, for example, the size of fish is small, Int. J. Comput. Vis. 12, 43–77. https://doi.org/10.1007/BF01420984.
Ben Tamou, A., Benzinou, A., Nasreddine, K., 2021. Multi-stream fish detection in
and the number of distractors in the tracking process is large. It unconstrained underwater videos by the fusion of two convolutional neural network
can be considered to introduce techniques such as transfer detectors. Appl. Intell. 51, 5809–5821. https://doi.org/10.1007/s10489-020-02155-
learning and adversarial learning to improve the effectiveness of 8.
Bertinetto, L., Valmadre, J., Henriques, J.F., Vedaldi, A., Torr, P.H.S., 2016. Fully-
feature extraction, thereby improving the identifiability and
convolutional Siamese networks for object tracking. In: Eur. Conf. Comput. Vis., pp.
distinguishability of fish. 850–865. doi: 10.1007/978-3-319-48881-3_56.
(2) The problem of prolonged tracking of fish. At present, most fish Beyan, C., Katsageorgiou, V.M., Fisher, R.B., 2018. Extracting statistically significant
behaviour from fish tracking data with and without large dataset cleaning. IET
tracking algorithms solve the problem of short-term tracking Comput. Vis. 12, 162–170. https://doi.org/10.1049/iet-cvi.2016.0462.
under a single challenge. For example, the algorithm only has an Bianchi, E., Dalzochio, T., Simo˜es, L.A.R., Rodrigues, G.Z.P., Silva, C.E.M., Gehlen, G.,
obvious effect on one case of illumination change, scale change or Nascimento, C.A., Spilki, F.R., Ziulkoski, A.L., Silva, L.B., 2019. Water quality
monitoring of the Sinos River Basin, Southern Brazil, using physicochemical and
ambiguity. Few algorithms can satisfy long time target tracking
microbiological analysis and biomarkers in laboratory-exposed fish. Ecohydrol.
under multiple challenges at the same time. Therefore, it is the Hydrobiol. 19, 328–338. https://doi.org/10.1016/j.ecohyd.2019.05.002.
future trend to study the algorithm that can track fish for a long Bochkovskiy, A., Wang, C., Liao, H.M., 2020. YOLOv4: optimal speed and accuracy of
object detection. doi: 10.48550/arXiv.2004.10934.
time under various influencing factors.
Bolme, D.S., Beveridge, J.R., Draper, B.A., Lui, Y.M., 2010. Visual object tracking using
(3) Design a lightweight model suitable for fish tracking algorithms. adaptive correlation filters. In: Proc. IEEE Comput. Soc. Conf. Comput. Vis. Pattern
Taking the Siamese network as an example, although good results Recognit, pp. 2544–2550. doi: 10.1109/CVPR.2010.5539960.
have been achieved in tracking accuracy and speed, these algo- Bondad-Reantaso, M.G., Subasinghe, R.P., Arthur, J.R., Ogawa, K., Chinabut, S.,
Adlard, R., Tan, Z., Shariff, M., 2005. Disease and health management in Asian
rithms generally require large storage space, which is not aquaculture. Vet. Parasitol. 132, 249–272. https://doi.org/10.1016/j.
conducive to practical applications. Therefore, technologies such vetpar.2005.07.005.
as knowledge distillation and network pruning can be considered Boom, B.J., Huang, P.X., He, J.Y., Fisher, R.B., 2012. Supporting Ground-Truth
annotation of image datasets using clustering. In: Int. Conf. Pattern Recognit. (ICPR
to be introduced into the algorithm in the future. Then, a target 2012), 1542–1545.
tracking network model with simplified structure and low Breitenstein, M.D., Reichlin, F., Leibe, B., Koller-Meier, E., Van Gool, L., 2011. Online
complexity is constructed. In addition, a neural network search multiperson tracking-by-detection from a single, uncalibrated camera. IEEE Trans.
Pattern Anal. Mach. Intell. 33, 1820–1833. https://doi.org/10.1109/
method can also be used to obtain a model structure that com-
TPAMI.2010.232.
bines low memory and high precision. Cheng, S., Zhao, K., Zhang, D., 2019. Abnormal water quality monitoring based on visual
sensing of three-dimensional motion behavior of fish. Symmetry (Basel) 11, 1–20.
https://doi.org/10.3390/sym11091179.
Furthermore, Transformers focus on global information and are able
Cong, H., Sun, M., Zhou, D., Zhao, X., 2016. Multi-target tracking of zebrafish based on
to model long-range dependencies. It can be combined with CNNs with particle filter. In: Chinese Control Conf. CCC, pp. 10308–10313. doi: 10.1109/
weak ability to capture global information to jointly improve the ChiCC.2016.7554987.
Danelljan, M., Hager, G., Khan, F.S., Felsberg, M., 2015. Learning spatially regularized
framework of tracking networks. It opens up a wider range of ideas in
correlation filters for visual tracking. In: Proc. IEEE Int. Conf. Comput. Vis. 2015
the field of object tracking. The visual tracking algorithm based on the Inter, pp. 4310–4318. doi: 10.1109/ICCV.2015.490.
above method will have a great space for exploration in future fish Danelljan, M., Robinson, A., Khan, F.S., Felsberg, M., 2016b. Beyond correlation filters:
tracking. learning continuous convolution operators for visual tracking. In: Lect. Notes
Comput. Sci. (including Subser. Lect. Notes Artif. Intell. Lect. Notes Bioinformatics)
9909 LNCS, pp. 472–488. doi: 10.1007/978-3-319-46454-1_29.
Danelljan, M., Hager, G., Khan, F.S., Felsberg, M., 2016a. Convolutional features for
Declaration of Competing Interest correlation filter based visual tracking. In: Proc. IEEE Int. Conf. Comput. Vis., pp.
621–629. doi: 10.1109/ICCVW.2015.84.
Dell, A.I., Bender, J.A., Branson, K., Couzin, I.D., de Polavieja, G.G., Noldus, L.P.J.J.,
The authors declare that they have no known competing financial P´erez-Escudero, A., Perona, P., Straw, A.D., Wikelski, M., Brose, U., 2014.
interests or personal relationships that could have appeared to influence Automated image-based tracking and its application in ecology. Trends Ecol. Evol.
the work reported in this paper. 29, 417–428. https://doi.org/10.1016/j.tree.2014.05.004.
Delpiano, J., Pizarro, L., Verschae, R., Ruiz-del-Solar, J., 2016. Multi-objective
optimization for parameter selection and characterization of optical flow methods.
Data availability Appl. Soft Comput. J. 46, 1067–1078. https://doi.org/10.1016/j.asoc.2016.01.037.
Ebrahimi, S.H., Ossewaarde, M., Need, A., 2021. Smart fishery: a systematic review and
research agenda for sustainable fisheries in the age of ai. Sustain. 13 (11), 6037.
No data was used for the research described in the article.
https://doi.org/10.3390/su13116037.
Edwards, P., 2015. Aquaculture environment interactions: past, present and likely future
Acknowledgments trends. Aquaculture 447, 2–14. https://doi.org/10.1016/j.aquaculture.2015.02.001.
Enze, Y., Miura, Y., 2020. Inter-frame differencing in training data for artificial
intelligence: contour processing for inter-frame differencing method. In: 2020 IEEE
This work was supported by the National Science Foundation of Int. Conf. Consum. Electron. - Taiwan, ICCE-Taiwan 2020, pp. 3–4. doi: 10.1109/
China ‘Analysis and feature recognition on feeding behavior of fish ICCE-Taiwan49838.2020.9258108.
Føre, M., Alfredsen, J.A., Gronningsater, A., 2011. Development of two telemetry-based
school in facility farming based on machine vision’ (No. 62076244) and
systems for monitoring the feeding behaviour of Atlantic salmon (Salmo salar L.) in
University-Local government Integration Development Project for Yan- aquaculture sea-cages. Comput. Electron. Agric. 76, 240–251. https://doi.org/
tai (No. 2020XDRHXMPT10). 10.1016/j.compag.2011.02.003.
Galoogahi, H.K., Fagg, A., Lucey, S., 2017. Learning background-aware correlation filters
for visual tracking. In: Proc. IEEE Int. Conf. Comput. Vis., pp. 1144–1152. doi:
References 10.1109/ICCV.2017.129.
Gaude, G.S., Borkar, S., 2019. Fish detection and tracking for turbid underwater video.
In: 2019 Int. Conf. Intell. Comput. Control Syst. ICCS 2019, pp. 326–331. doi:
An, D., Huang, J., Wei, Y., 2021. A survey of fish behaviour quantification indexes and
methods in aquaculture. Rev. Aquac. 13, 2169–2189. https://doi.org/10.1111/ 10.1109/ICCS45141.2019.9065425.
Goyal, K., Singhai, J., 2018. Review of background subtraction methods using Gaussian
raq.12564. mixture model for video surveillance systems. Artif. Intell. Rev. 50, 241–259.
Anas, O., Wageeh, Y., Mohamed, H.E.D., Fadl, A., ElMasry, N., Nabil, A., Atia, A., 2020.
https://doi.org/10.1007/s10462-017-9542-x.
Detecting abnormal fish behavior using motion trajectories in ubiquitous
environments. Proc. Comput. Sci. 175, 141–148. https://doi.org/10.1016/j. Han, F., Zhu, J., Liu, B., Zhang, B., Xie, F., 2020. Fish shoals behavior detection based on
convolutional neural network and spatiotemporal information. IEEE Access 8,
procs.2020.07.023. 126907–126926. https://doi.org/10.1109/ACCESS.2020.3008698.
Barnich, O., Droogenbroeck, M.V., 2009. VIBE: a powerful random technique to estimate
He, H., Ma, S.C., Sun, L., 2018. Multi-moving target detection based on the combination
the background in video sequences. In: Int. Conf. Acoust. Speech Signal Process, pp.
945–948. o Wf Rth Cr e Se
y
mfr pa .m Ae
d
d vi .f f Re ore bn oc t.e Aa ulg to or mit .h Wm
R
a Cn d
S
Ab Rac Ak g 2r 0o 1u 8n d
-
Pd ri off ce er ee dn ic ne
g
,a l pg po .r i 1t 5h 3m –.
1
I 5n 8: .2 d0 o1 i8
:
Barreiros, M.O., Dantas, D.O., Silva, L.C.O., Ribeiro, S., Barros, A.K., 2021. Zebrafish
10.1109/WRC-SARA.2018.8584221.
tracking using YOLOv2 and Kalman filter. Sci. Rep. 11 (1) https://doi.org/10.1038/
s41598-021-81997-9.
16

# Page 17

Y. Mei et al. C o m p u t e r s a n d E l e c t r o n ic s i n A g r i c u l t u r e 201(2022)107335
Hedgepeth, J.B., Fuhrimn, D., Cronkite, G.M.W., Xie, Y., Mulligan, T.J., 2000. A tracking Li, Y.Y., Sun, L.Q., Zou, Y.B., Li, Y., 2017. Individual pig object detection algorithm based
transducer for following fish movement in shallow water and at close range. Aquat. on Gaussian mixture model. Int. J. Agric. Biol. Eng. 10, 186–193. https://doi.org/
Living Resour. 13, 305–311. https://doi.org/10.1016/S0990-7440(00)01089-5. 10.25165/j.ijabe.20171005.3136.
Henriques, J.F., Caseiro, R., Martins, P., Batista, J., 2015. High-speed tracking with Li, F., Tian, C., Zuo, W., Zhang, L., Yang, M.H., 2018b. Learning spatial-temporal
kernelized correlation filters. IEEE Trans. Pattern Anal. Mach. Intell. 37, 583–596. regularized correlation filters for visual tracking. In: Proc. IEEE Comput. Soc. Conf.
https://doi.org/10.1109/TPAMI.2014.2345390. Comput. Vis. Pattern Recognit, pp. 4904–4913. doi: 10.1109/CVPR.2018.00515.
Hossain, E., Alam, S.M.S., Ali, A.A., Amin, M.A., 2016. Fish activity tracking and species Li, D., Wang, Z., Wu, S., Miao, Z., Du, L., Duan, Y., 2020b. Automatic recognition
identification in underwater video. In: 2016 5th Int. Conf. Informatics, Electron. methods of fish feeding behavior in aquaculture: a review. Aquaculture 528,
Vision, ICIEV 2016, pp. 62–66. doi: 10.1109/ICIEV.2016.7760189. 735508. https://doi.org/10.1016/j.aquaculture.2020.735508.
Hou, Y., Zou, X., Tang, W., Jiang, W., Zhu, J., Deng, C., Zhang, Y., 2019. Precise capture Li, B., Yan, J., Wu, W., Zhu, Z., Hu, X., 2018a. High performance visual tracking with
of fish movement trajectories in complex environments via ultrasonic signal tag siamese region proposal network. In: Proc. IEEE Comput. Soc. Conf. Comput. Vis.
tracking. Fish. Res. 219, 105307 https://doi.org/10.1016/j.fishres.2019.105307. Pattern Recognit., pp. 8971–8980. doi: 10.1109/CVPR.2018.00935.
Hsia, C.H., Liou, Y.J., Chiang, J.S., 2016. Directional prediction camshift algorithm based Liu, Z., Li, X., Fan, L., Lu, H., Liu, L., Liu, Y., 2014. Measuring feeding activity of fish in
on adaptive search pattern for moving object tracking. J. Real-Time Image Process. RAS using computer vision. Aquac. Eng. 60, 20–27. https://doi.org/10.1016/j.
12, 183–195. https://doi.org/10.1007/s11554-013-0382-x. aquaeng.2014.03.005.
Hsiao, Y.H., Chen, C.C., 2016. A sparse sample collection and representation method Liu, C., Shui, P., Li, S., 2011. Unscented extended kalman filter for target tracking.
using re-weighting and dynamically updating OMP for fish tracking. In: Proc. - Int. J. Syst. Eng. Electron. 22, 188–192. https://doi.org/10.3969/j.issn.1004-
Conf. Image Process. ICIP 2016-August, pp. 3494–3497. doi: 10.1109/ 4132.2011.02.002.
ICIP.2016.7533009. Lopez-Marcano, S., Jinks, E.L., Buelow, C.A., Brown, C.J., Wang, D., Kusy, B., Ditria, E.
Huang, T.W., Hwang, J.N., Romain, S., Wallace, F., 2019. Fish tracking and segmentation M., Connolly, R.M., 2021. Automatic detection of fish and tracking of movement for
from stereo videos on the wild sea surface for electronic monitoring of rail fishing. ecology. Ecol. Evol. 11 (12), 8254–8263.
IEEE Trans. Circuits Syst. Video Technol. 29, 3146–3158. https://doi.org/10.1109/ Lumauag, R., Nava, M., 2018. Fish tracking and counting using image processing. In:
TCSVT.2018.2872575. 2018 IEEE 10th Int. Conf. Humanoid, Nanotechnology, Inf. Technol. Commun.
Isard, M., Blake, A., 1998. Confensation-conditional density propagation for visual Control. Environ. Manag. doi: 10.1109/HNICEM.2018.8666369.
tracking. Int. J. Comput. Vis. 29, 5–28. Ma, C., Huang, J. Bin, Yang, X., Yang, M.H., 2015. Hierarchical convolutional features
Jager, J., Wolff, V., Fricke-Neuderth, K., Mothes, O., Denzler, J., 2017. Visual fish for visual tracking. In: Proc. IEEE Int. Conf. Comput. Vis. 2015 Inter, pp. 3074–3082.
tracking: combining a two-stage graph approach with CNN-features. In: Ocean. 2017 doi: 10.1109/ICCV.2015.352.
- Aberdeen 2017-Octob, 1–6. doi: 10.1109/OCEANSE.2017.8084691. Mao, J.F., Gang, X., Sheng, W.G., Liu, X.H., IEEE, 2015. A 3D occlusion tracking Model of
Jalal, A., Salman, A., Mian, A., Shortis, M., Shafait, F., 2020. Fish detection and species the underwater fish targets. In: 2015 IEEE Int. Conf. Electro/Information Technol.
classification in underwater environments using deep learning with temporal Martins, C.I.M., Galhardo, L., Noble, C., Damsgård, B., Spedicato, M.T., Zupa, W.,
information. Ecol. Inform. 57, 101088 https://doi.org/10.1016/j. Beauchaud, M., Kulczykowska, E., Massabuau, J.C., Carter, T., Planellas, S.R.,
ecoinf.2020.101088. Kristiansen, T., 2012. Behavioural indicators of welfare in farmed fish. Fish Physiol.
Jang, J., Jiang, H., 2021. MeanShift++: Extremely fast mode-seeking with applications Biochem. 38, 17–41. https://doi.org/10.1007/s10695-011-9518-8.
to segmentation and object tracking. In: Proc. IEEE Comput. Soc. Conf. Comput. Vis. Marti-Puig, P., Serra-Serra, M., Campos-Candela, A., Reig-Bolano, R., Manjabacas, A.,
Pattern Recognit., pp. 4100–4111. doi: 10.1109/CVPR46437.2021.00409. Palmer, M., 2018. Quantitatively scoring behavior from video-recorded, long-lasting
Jiang, Y., Fang, J., Li, Z., Yue, J., Wang, Z., Li, D., 2013. Automatic tracking of swimming fish trajectories. Environ. Model. Softw. 106, 68–76. https://doi.org/10.1016/j.
koi using a particle filter with a center-surrounding cue. Math. Comput. Model. 58, envsoft.2018.01.007.
859–867. https://doi.org/10.1016/j.mcm.2012.12.015. Marvasti-Zadeh, S.M., Cheng, L., Ghanei-Yakhdan, H., Kasaei, S., 2022. Deep learning for
Jing, D., Han, J., Wang, X., Wang, G., Tong, J., Shen, W., Zhang, J., 2017. A method to visual tracking: a comprehensive survey. IEEE Trans. Intell. Transp. Syst. 23,
estimate the abundance of fish based on dual-frequency identification sonar 3943–3968. https://doi.org/10.1109/TITS.2020.3046478.
(DIDSON) imaging. Fish. Sci. 83, 685–697. https://doi.org/10.1007/s12562-017- Masser, M., 1992. Management of recreational fish ponds in Alabama. ACES Pap. No.
1111-3. ANR-0577 AL: ACES, Auburn.
Kang, K., Ouyang, W., Li, H., Wang, X., 2016. Object detection from video tubelets with Mizuno, K., Liu, X., Asada, A., Ashizawa, J., Fujimoto, Y., Shimada, T., 2015. Application
convolutional neural networks. In: Proc. IEEE Comput. Soc. Conf. Comput. Vis. of a high-resolution acoustic video camera to fish classification: an experimental
Pattern Recognit. 2016-Decem, pp. 817–825. doi: 10.1109/CVPR.2016.95. study. In: 2015 IEEE Underw. Technol. UT 2015. doi: 10.1109/UT.2015.7108250.
Kim, K., Chalidabhongse, T.H., Harwood, D., Davis, L., 2005. Real-time foreground- Morais, E.F., Campos, M.F.M., P´adua, F.L.C., Carceroni, R.L., 2005. Particle filter-based
background segmentation using codebook model. Real-Time Imaging 11, 172–185. predictive tracking for robust fish counting. In: Brazilian Symp. Comput. Graph.
https://doi.org/10.1016/j.rti.2004.12.004. Image Process. 2005, pp. 367–374. doi: 10.1109/SIBGRAPI.2005.36.
Konovalov, D.A., Saleh, A., Bradley, M., Sankupellay, M., Marini, S., Sheaves, M., 2019. Nair, R.S., Domnic, S., 2022. A combination of learning and non-learning based method
Underwater fish detection with weak multi-domain supervision. In: Proc. Int. Jt. for enhancement, compression and reconstruction of underwater images. Aquac.
Conf. Neural Networks 2019-July, pp. 14–19. doi: 10.1109/IJCNN.2019.8851907. Fish. 7, 201–210. https://doi.org/10.1016/j.aaf.2021.10.006.
Krizhevsky, A., Sutskever, I., Hinton, G.., 2012. ImageNet classification with deep Nam, H., Han, B., 2016. Learning multi-domain convolutional neural networks for visual
convolutional neural networks. Adv. Neural Inf. Process. Syst. 1097–1105. tracking. In: Proc. IEEE Comput. Soc. Conf. Comput. Vis. Pattern Recognit. 2016-
Lai, Y.C., Huang, R.J., Kuo, Y.P., Tsao, C.Y., Wang, J.H., Chang, C.C., 2019. Underwater Decem, pp. 4293–4302. doi: 10.1109/CVPR.2016.465.
target tracking via 3D convolutional networks. In: 2019 IEEE 6th Int. Conf. Ind. Eng. Pan, Z., Liu, S., Fu, W., 2017. A review of visual moving target tracking. Multimed. Tools
Appl. ICIEA 2019, pp. 485–490. doi: 10.1109/IEA.2019.8715217. Appl. 76, 16989–17018. https://doi.org/10.1007/s11042-016-3647-0.
Lan, Y., Ji, Z., Gao, J., Wang, Y., 2014. Robot fish detection based on a combination Papadakis, V.M., Papadakis, I.E., Lamprianidou, F., Glaropoulos, A., Kentouri, M., 2012.
method of three-frame-difference and background subtraction. In: 26th Chinese A computer-vision system and methodology for the analysis of fish behavior. Aquac.
Control Decis. Conf. CCDC 2014, pp. 3905–3909. doi: 10.1109/ Eng. 46, 53–59. https://doi.org/10.1016/j.aquaeng.2011.11.002.
CCDC.2014.6852862. Park, H., 2021. α-MeanShift++: improving MeanShift++for image segmentation. IEEE
Lecun, Y., 1989. Generalization and network design strategies. Int. CONF Connect. Access 9, 131430–131439. https://doi.org/10.1109/ACCESS.2021.3114223.
Perspect. 143–155. Pedersen, M., Haurum, J.B., Bengtson, S.H., Moeslund, T.B., 2020. 3D-ZEF: a 3D
Lee, J.Y., Lee, J.W., Talluri, T., Angani, A., Lee, J.B., 2020. Realization of robot fish with zebrafish tracking benchmark dataset. In: Proc. IEEE Comput. Soc. Conf. Comput.
3D hologram fish using augmented reality. In: 2nd IEEE Int. Conf. Archit. Constr. Vis. Pattern Recognit., pp. 2423–2433. doi: 10.1109/CVPR42600.2020.00250.
Environ. Hydraul. 2020, ICACEH 2020, Vol. 32, pp. 102–104. doi: 10.1109/ Pinkiewicz, T., Williams, R., Purser, J., 2008. Application of the particle filter to tracking
ICACEH51803.2020.9366226. of fish in aquaculture research. In: Proc. - Digit. Image Comput. Tech. Appl. DICTA
Li, D., Du, L., 2021. Recent advances of deep learning algorithms for aquacultural 2008, pp. 457–464. doi: 10.1109/DICTA.2008.28.
machine vision systems with emphasis on fish. Artif Intell Rev 55 (5), 4077–4116. Pursche, A.R., Walsh, C.T., Taylor, M.D., 2014. Evaluation of a novel external tag-mount
Li, B., Wu, W., Wang, Q., Zhang, F., Xing, J., Yan, J., 2019. SIAMRPN++: evolution of for acoustic tracking of small fish. Fish. Manag. Ecol. 21, 169–172. https://doi.org/
siamese visual tracking with very deep networks. In: Proc. IEEE Comput. Soc. Conf. 10.1111/fme.12051.
Comput. Vis. Pattern Recognit. 2019-June, pp. 4277–4286. doi: 10.1109/ Qian, Z.M., Wang, S.H., Cheng, X.E., Chen, Y.Q., 2016. An effective and robust method
CVPR.2019.00441. for tracking multiple fish in video image based on fish head detection. BMC Bioinfor.
Li, D., Hao, Y., Duan, Y., 2020a. Nonintrusive methods for biomass estimation in 17, 1–11. https://doi.org/10.1186/s12859-016-1138-y.
aquaculture with emphasis on fish: a review. Rev. Aquac. 12, 1390–1411. https:// Qu, Z., Huang, X.L., 2017. The foreground detection algorithm combined the
doi.org/10.1111/raq.12388. temporal–spatial information and adaptive visual background extraction. Imaging
Li, Q., Li, R., Ji, K., Dai, W., 2016. Kalman filter and its application. In: Proc. - 8th Int. Sci. J. 65, 49–61. https://doi.org/10.1080/13682199.2016.1258509.
Conf. Intell. Networks Intell. Syst. ICINIS 2015, pp. 74–77. doi: 10.1109/ Redmon, J., Farhadi, A., 2018. YOLOv3: an incremental improvement.
ICINIS.2015.35. Redmon, J., Farhadi, A., 2016. Yolo V2.0. Cvpr2017, pp. 187–213.
Li, X., Ma, D., Yin, B., 2021. Advance research in agricultural text-to-speech: the word Ren, S., He, K., Girshick, R., Sun, J., 2017. Faster R-CNN: towards real-time object
segmentation of analytic language and the deep learning-based end-to-end system. detection with region proposal networks. IEEE Trans. Pattern Anal. Mach. Intell. 39,
Comput. Electron. Agric. 180, 105908 https://doi.org/10.1016/j. 1137–1149. https://doi.org/10.1109/TPAMI.2016.2577031.
compag.2020.105908. Rodríguez, A´ ., Bermúdez, M., Rabun˜al, J.R., Puertas, J., 2015. Fish tracking in vertical
Li, L., Song, J.Y., Yan, Z.Y., 2014. Moving object detection based on the fish. Appl. Mech. slot fishways using computer vision techniques. J. Hydroinformatics 17, 275–292.
Mater. 644–650, 1253–1256. https://doi.org/10.4028/www.scientific.net/ https://doi.org/10.2166/hydro.2014.034.
AMM.644-650.1253.
17

# Page 18

Y. Mei et al. C o m p u t e r s a n d E l e c t r o n ic s i n A g r i c u l t u r e 201(2022)107335
Saberioon, M.M., Cisar, P., 2016. Automated multiple fish tracking in three-Dimension Wu, T.H., Huang, Y.I., Chen, J.M., 2015. Development of an adaptive neural-based fuzzy
using a Structured Light Sensor. Comput. Electron. Agric. 121, 215–221. https://doi. inference system for feeding decision-making assessment in silver perch (Bidyanus
org/10.1016/j.compag.2015.12.014. bidyanus) culture. Aquac. Eng. 66, 41–51. https://doi.org/10.1016/j.
Saberioon, M., Gholizadeh, A., Cisar, P., Pautsina, A., Urban, J., 2017. Application of aquaeng.2015.02.001.
machine vision systems in aquaculture with emphasis on fish: state-of-the-art and Xia, C., Fu, L., Liu, Z., Liu, H., Chen, L., Liu, Y., 2018. Aquatic toxic analysis by
key issues. Rev. Aquac. 9, 369–387. https://doi.org/10.1111/raq.12143. monitoring fish behavior using computer vision: a recent progress. J. Toxicol. 2018,
Sadoul, B., Evouna Mengues, P., Friggens, N.C., Prunet, P., Colson, V., 2014. A new 1–11.
method for measuring group behaviours of fish shoals from recorded videos taken in Xiao, G., Zhang, W., Zhang, Y.L., Chen, J.J., Huang, S.S., Zhu, L.M., 2011. Online
near aquaculture conditions. Aquaculture 430, 179–187. https://doi.org/10.1016/j. monitoring system of fish behavior. In: Int. Conf. Control. Autom. Syst., pp.
aquaculture.2014.04.008. 1309–1312.
Salman, A., Maqbool, S., Khan, A.H., Jalal, A., Shafait, F., 2019. Real-time fish detection Xiao, G., Fan, W.K., Mao, J.F., Cheng, Z.B., Zhong, D.H., Li, Y., 2017. Research of the fish
in complex backgrounds using probabilistic background modelling. Ecol. Inform. 51, tracking method with occlusion based on monocular stereo vision. In: Proc. - 2016
44–51. https://doi.org/10.1016/j.ecoinf.2019.02.011. Int. Conf. Inf. Syst. Artif. Intell. ISAI 2016, pp. 581–589. doi: 10.1109/
Sapijaszko, G., Mikhael, W.B., 2018. An overview of recent convolutional neural network ISAI.2016.0129.
algorithms for image recognition. In: 2018 IEEE 61ST Int. MIDWEST Symp. Xiao, Y., Tian, Z., Yu, J., Zhang, Y., Liu, S., Du, S., Lan, X., 2020. A review of object
CIRCUITS Syst., pp. 743–746. detection based on deep learning. Multimed. Tools Appl. 79, 23729–23791. https://
Sengar, S.S., Mukhopadhyay, S., 2017. Moving object detection based on frame doi.org/10.1007/s11042-020-08976-6.
difference and W4. Signal, Image Video Process. 11, 1357–1364. https://doi.org/ Xiao, M., Zhang, L., Han, C.Z., 2005. A moving detection algorithm based on space-time
10.1007/s11760-017-1093-8. background difference. Adv. Intell. Comput. PT 1 Proc. 3644, 146–154.
Shantaiya, S., Verma, K., Mehta, K., 2015. Multiple object tracking using kalman filter Xin, L., Wei, X., 2015. Object tracking using meanshift algorithm combined with Kalman
and optical flow. Eur. J. Adv. Eng. Technol. 2, 34–39. https://doi.org/10.1016/j. filter on robotic fish. In: Proc. 5th Int. Symp. Knowl. Acquis. Model., Vol. 80, pp.
eswa.2016.06.020. 168–172. doi: 10.2991/kam-15.2015.46.
Sharif, M.H., Galip, F., Guler, A., Uyaver, S., 2016. A simple approach to count and track Xu, Z., Cheng, X.E., 2017. Zebrafish tracking using convolutional neural networks. Sci.
underwater fishes from videos. In: 2015 18th Int. Conf. Comput. Inf. Technol. ICCIT Rep. 7, 1–11. https://doi.org/10.1038/srep42815.
2015, pp. 347–352. doi: 10.1109/ICCITechn.2015.7488094. Xu, Y., Wang, Z., Li, Z., Yuan, Y., Yu, G., 2020b. SiamFC++: Towards robust and accurate
Shevchenko, V., Eerola, T., Kaarna, A., 2018. Fish detection from low visibility visual tracking with target estimation guidelines. In: AAAI 2020 - 34th AAAI Conf.
underwater videos. In: Proc. - Int. Conf. Pattern Recognit. 2018-Augus, pp. Artif. Intell., pp. 12549–12556. doi: 10.1609/aaai.v34i07.6944.
1971–1976. doi: 10.1109/ICPR.2018.8546183. Xu, N., Yang, L., Fan, Y., Yang, J., Yue, D., Liang, Y., Price, B., Cohen, S., Huang, T., 2018.
Shi, H.H., Xiang, W., 2013. Object tracking using improved meanshift algorithm YouTube-VOS: sequence-to-sequence video object segmentation. In: Eur. Conf.
combined with Kalman filter on independent visual robotic fish. Appl. Mech. Mater. Comput. Vis. 11209 LNCS, pp. 603–619. doi: 10.1007/978-3-030-01228-1_36.
333–335, 1030–1033. https://doi.org/10.4028/www.scientific.net/AMM.333- Xu, W., Zhu, Z., Ge, F., Han, Z., Li, J., 2020a. Analysis of behavior trajectory based on
335.1030. deep learning in ammonia environment for fish. Sensors (Switzerland) 20, 1–11.
Shiau, Y.-H., Chen, C.-C., Lin, S.-I., 2013. Using bounding-surrounding boxes method for https://doi.org/10.3390/s20164425.
fish tracking in real world underwater observation. Int. J. Adv. Robot. Syst. 10 (7), Yang, S., Hao, K., Ding, Y., Liu, J., 2018a. Improved visual background extractor with
298. adaptive range change. Memetic Comput. 10, 53–61. https://doi.org/10.1007/
Shin, K.J., Musunuri, Y.R., 2017. Realization of aquarium robot holographic world using s12293-017-0225-6.
3 axes tracking optical flow detecting method. In: FTC 2016 - Proc. Futur. Technol. Yang, S.C., Lin, G.C., Wang, C.M., 2018b. Foreground detection using texture-based
Conf., pp. 916–922. doi: 10.1109/FTC.2016.7821712. codebook method for monitoring systems. Signal Image Video Process. 12, 693–701.
Spampinato, C., Chen-Burger, Y.H., Nadarajan, G., Fisher, R.B., 2008. Detecting, tracking https://doi.org/10.1007/s11760-017-1209-1.
and counting fish in low quality unconstrained underwater videos. VISAPP 2008–3rd Yang, L., Liu, Y., Yu, H., Fang, X., Song, L., Li, D., Chen, Y., 2021. Computer vision
Int. Conf. Comput. Vis. Theory Appl. Proc. 2, 514–519. https://doi.org/10.5220/ models in intelligent aquaculture with emphasis on fish detection and behavior
0001077705140519. analysis: a review. Arch. Comput. Methods Eng. 28, 2785–2816. https://doi.org/
Spampinato, C., Palazzo, S., Boom, B., Van Ossenbruggen, J., Kavasidis, I., Di Salvo, R., 10.1007/s11831-020-09486-2.
Lin, F.P., Giordano, D., Hardman, L., Fisher, R.B., 2014. Understanding fish behavior Yao, H., 2021. A survey for target tracking on meanshift algorithms. In: 2021 IEEE Int.
during typhoon events in real-life underwater environments. Multimed. Tools Appl. Conf. Consum. Electron. Comput. Eng., pp. 476–479. doi: 10.1109/
70, 199–236. https://doi.org/10.1007/s11042-012-1101-5. ICCECE51280.2021.9342102.
Tang, Y., Dananjayan, S., Hou, C., Guo, Q., Luo, S., He, Y., 2021. A survey on the 5G Yao, J., Qi, J., Zhang, J., Shao, H., Yang, J., Li, X., 2021. A real-time detection algorithm
network and its impact on agriculture: challenges and opportunities. Comput. for kiwifruit defects based on yolov5. Electron. 10 (14), 1711.
Electron. Agric. 180, 105895 https://doi.org/10.1016/j.compag.2020.105895. Yazdi, M., Bouwmans, T., 2018. New trends on moving object detection in video images
Terayama, K., Hioki, H., Sakagami, M., 2017. Measuring tail beat frequency and coast captured by a moving camera: a survey. Comput. Sci. Rev. 28, 157–177. https://doi.
phase in school of fish for collective motion analysis. In: Eighth Int. Conf. Graph. org/10.1016/j.cosrev.2018.03.001.
Image Process. (ICGIP 2016), pp. 10225, 102251R. doi: 10.1117/12.2266447. Yi, X., Chen, Z., 2019. A robust visual tracking method for unmanned mobile systems.
Terayama, K., Hioki, H., Sakagami, M.A., 2015. A measurement method for speed J. Dyn. Syst. Meas. Control. Trans. ASME. 141, 1–8. https://doi.org/10.1115/
distribution of collective motion with optical flow and its application to estimation 1.4043119.
of rotation curve. In: Proc. - 2014 IEEE Int. Symp. Multimedia, ISM 2014, pp. 32–39. Yue, K., Shen, Y., 2022. An overview of disruptive technologies for aquaculture. Aquac.
doi: 10.1109/ISM.2014.26. Fish. 7, 111–120. https://doi.org/10.1016/j.aaf.2021.04.009.
Verdal, H., Komen, H., Quillet, E., Chatain, B., Allal, F., Benzie, J.A.H., Vandeputte, M., Zhang, Y., Zheng, J., Zhang, C., Li, B., 2018. An effective motion object detection method
2018. Improving feed efficiency in fish using selective breeding: a review. Rev. using optical flow estimation under a moving camera. J. Vis. Commun. Image
Aquac. 10, 833–851. https://doi.org/10.1111/raq.12202. Represent. 55, 215–228. https://doi.org/10.1016/j.jvcir.2018.06.006.
Vo, T.T.E., Ko, H., Huh, J.H., Kim, Y., 2021. Overview of smart aquaculture system: Zhao, J., Gu, Z., Shi, M., Lu, H., Li, J., Shen, M., Ye, Z., Zhu, S., 2016. Spatial behavioral
Focusing on applications of machine learning and computer vision. Electron. 10, characteristics and statistics-based kinetic energy modeling in special behaviors
1–26. https://doi.org/10.3390/electronics10222882. detection of a shoal of fish in a recirculating aquaculture system. Comput. Electron.
Wang, N., Yeung, D., 2013. Learning a deep compact image representation for visual Agric. 127, 271–280. https://doi.org/10.1016/j.compag.2016.06.025.
tracking. Curran Assoc. Inc. doi: 10.1128/iai.62.9.3723-3730.1994. Zhao, X., Yan, S., Gao, Q., 2019. An algorithm for tracking multiple fish based on
Wang, G., Hwang, J.N., Williams, K., Cutter, G., 2017a. Closed-loop tracking-by- biological water quality monitoring. IEEE Access 7, 15018–15026. https://doi.org/
detection for ROV-based multiple fish tracking. In: Proc. - 2nd Work. Comput. Vis. 10.1109/ACCESS.2019.2895072.
Anal. Underw. Imagery, CVAUI 2016 - Conjunction with Int. Conf. Pattern Zhou, A., Cheng, S., Pan, Q.B., Sun, D.Y., 2016. An optimal algorithm based on extended
Recognition, ICPR 2016, pp. 7–12. doi: 10.1109/CVAUI.2016.17. kalman filter and the data fusion for infrared touch overlay. In: Int. Symp. Precis.
Wang, G., Hwang, J.N., Williams, K., Wallace, F., Rose, C.S., 2017b. Shrinking encoding Mech. Meas., pp. 9903. doi: 10.1117/12.2218681.
with two-level codebook learning for fine-grained fish recognition. In: Proc. - 2nd Zhou, H.B., Xiao, G., Chen, J.J., Gao, F., Ying, X.F., 2008. Real-time fish detection based
Work. Comput. Vis. Anal. Underw. Imagery, CVAUI 2016 - Conjunction with Int. on improved adaptive background. In: WSEAS Adv. Appl. Comput. Appl. Comput.
Conf. Pattern Recognition, ICPR 2016, pp. 31–36. doi: 10.1109/CVAUI.2016.18. Sci.
Wang, J.H., Lee, S.K., Lai, Y.C., Lin, C.C., Wang, T.Y., Lin, Y.R., Hsu, T.H., Huang, C.W., Zhou, C., Lin, K., Xu, D., Chen, L., Guo, Q., Sun, C., Yang, X., 2018a. Near infrared
Chiang, C.P., 2020. Anomalous behaviors detection for underwater fish using AI computer vision and neuro-fuzzy model-based feeding decision system for fish in
techniques. IEEE Access 8, 224372–224382. https://doi.org/10.1109/ aquaculture. Comput. Electron. Agric. 146, 114–124. https://doi.org/10.1016/j.
ACCESS.2020.3043712. compag.2018.02.006.
Wang, H., Zhang, S., Zhao, S., Wang, Q., Li, D., Zhao, R., 2022. Real-time detection and Zhou, C., Xu, D., Lin, K., Sun, C., Yang, X., 2018b. Intelligent feeding control methods in
tracking of fish abnormal behavior based on improved YOLOV5 and SiamRPN++. aquaculture with an emphasis on fish: a review. Rev. Aquac. 10, 975–993. https://
Comput. Electron. Agric. 192, 106512 https://doi.org/10.1016/j. doi.org/10.1111/raq.12218.
compag.2021.106512. Zhou, C., Xu, D., Chen, L., Zhang, S., Sun, C., Yang, X., Wang, Y., 2019. Evaluation of fish
Wang, S.H., Zhao, J.W., Chen, Y.Q., 2017c. Robust tracking of fish schools using CNN for feeding intensity in aquaculture using a convolutional neural network and machine
head identification. Multimed. Tools Appl. 76, 23679–23697. https://doi.org/ vision. Aquaculture 507, 457–465. https://doi.org/10.1016/j.
10.1007/s11042-016-4045-3. aquaculture.2019.04.056.
Wang, J., Zhao, M., Zou, L., Hu, Y., Cheng, X., Liu, X., 2019. Fish tracking based on Zhu, Z., Li, X., Wang, Z., He, L., He, B., Xia, S., 2020. Development and research of a
improved TLD algorithm in real-world underwater environment. Mar. Technol. Soc. multi-medium motion capture system for underwater intelligent agents. Appl. Sci. 10
J. 53 (3), 80–89. (18), 6237.
18

# Page 19

Y. Mei et al. C o m p u t e r s a n d E l e c t r o n ic s i n A g r i c u l t u r e 201(2022)107335
Zhu, Z., Wang, Q., Li, B., Wu, W., 2018. Distractor-aware siamese networks for visual Zolfaghari, M., Singh, K., Brox, T., 2018. ECO: efficient convolutional network for online
object tracking. In: Eur. Conf. Comput. Vis., pp. 1–17. video understanding. In: Lect. Notes Comput. Sci., pp. 713–730. doi: 10.1007/978-3-
Zivkovic, Z., 2004. Improved adaptive Gaussian mixture model for background 030-01216-8_43.
subtraction. Proc. - Int. Conf. Pattern Recognit. 2, 28–31. https://doi.org/10.1109/ Zou, L., Zhao, M., Cao, F., Zan, S., Cheng, X., Liu, X., 2021. Fish tracking based on feature
icpr.2004.1333992. fusion and scale adaptation in a real-world underwater environment. Mar. Technol.
Soc. J. 55 (2), 45–53.
19

