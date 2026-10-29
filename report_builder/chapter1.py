"""
Chapter 1 Builder for ClearDrive Tech PBL Report
Generates Pages 11 to 18:
1.1 Background & Real-World Motivation
1.2 Atmospheric Degradation & Optical Physics
1.3 The Driving Question
1.4 Project & Pedagogical Objectives
1.5 Scope, Boundaries, and Limitations
1.6 Regulatory & Safety Compliance Framework
"""

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib import colors
from report_builder.styles import (
    USABLE_WIDTH, COLOR_PRIMARY, COLOR_SECONDARY, COLOR_DARK, COLOR_MUTED,
    COLOR_BORDER, create_callout_box
)


def get_chapter1_flowables(styles):
    """Returns flowables for Chapter 1 (Pages 11 to 18)."""
    f = []

    # =========================================================================
    # PAGE 11: CHAPTER 1 COVER & 1.1 BACKGROUND
    # =========================================================================
    f.append(Paragraph("<b>CHAPTER 1</b>", styles['ChapterHeader']))
    f.append(Paragraph("<b>INTRODUCTION</b>", styles['DocTitle']))
    f.append(HRFlowable(width="100%", thickness=1.5, color=COLOR_PRIMARY, spaceBefore=4, spaceAfter=14))

    f.append(Paragraph("<b>1.1 Background and Real-World Motivation</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Vehicular transportation forms the vital circulatory backbone of modern economic infrastructure. "
        "However, road safety remains one of the most pressing public health and engineering crises of the twenty-first century. "
        "According to the official annual reports published by the Ministry of Road Transport and Highways (MoRTH), Government of India, "
        "the country witnesses over 4,60,000 recorded road accidents annually, claiming more than 1,68,000 human lives and inflicting permanent "
        "disabling injuries on over 4,40,000 citizens. This represents a staggering loss of approximately 3% of the national Gross Domestic Product (GDP). "
        "A disproportionately large percentage of these catastrophic fatalities occur during adverse environmental driving conditions, specifically "
        "characterized by dense aerosol fog, blinding torrential monsoon rain, pitch-black unlit rural corridors, and the blinding glare of oncoming "
        "aftermarket LED high-beam headlights.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "In developing nations such as India, geographic and climatic realities introduce acute operational hazards rarely addressed by western-centric "
        "autonomous driving systems. Across the vast Nilgiri mountain range and the Western Ghats—encompassing high-altitude highway corridors such as "
        "the Ooty Ghat Road (consisting of 36 extreme hairpin bends), the Valparai pass (40 hairpin curves), Coonoor, and Kodaikanal—dense orographic "
        "cloud immersion and sudden aerosol mist banks can reduce line-of-sight optical visibility to less than three meters in a matter of seconds. "
        "Under such extreme conditions, the human visual system suffers from catastrophic contrast degradation, loss of peripheral motion cues, and depth "
        "misperception, transforming routine mountain transits into fatal collision corridors.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "Similarly, throughout the winter months (November through February), the vast Gangetic plains of northern India, spanning major multi-lane "
        "expressways such as the Yamuna Expressway, the Eastern Peripheral Expressway, and National Highway 44, experience severe radiation fog mixed "
        "with industrial aerosols. These conditions routinely trigger horrific 20-to-40-vehicle chain-reaction pileups, resulting in mass casualties and "
        "complete economic arterial paralysis.",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 12: 1.1 CONTINUED — SENSOR DEFICITS IN THE REAL WORLD
    # =========================================================================
    f.append(Paragraph("<b>1.1.1 The Failure Modes of Contemporary Automotive Sensor Suites</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "To mitigate vehicular collisions, automotive original equipment manufacturers (OEMs) have introduced Advanced Driver Assistance Systems (ADAS). "
        "However, state-of-the-art enterprise ADAS solutions rely on physical sensor suites that exhibit fundamental, catastrophic physical failure modes "
        "when exposed to adverse weather:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>1. Light Detection and Ranging (LiDAR):</b> While 64-beam and 128-beam mechanical and solid-state LiDAR units deliver sub-centimeter 3D spatial "
        "reconstruction in dry, clear daylight, their operational wavelengths (typically 905 nm or 1550 nm) suffer from severe backscattering when encountering "
        "suspended aerosol water droplets and heavy rain sheets. The laser pulses reflect off raindrops and fog particles rather than roadway obstacles, "
        "generating tens of thousands of phantom 'noise points' that choke clustering algorithms and cause emergency braking lockups. Furthermore, high-end "
        "automotive LiDAR rigs cost upwards of Rs. 25,00,000 ($30,000), making them entirely unviable for commercial fleet adoption.",
        styles['BulletItem']
    ))
    f.append(Paragraph(
        "<b>2. Millimeter-Wave Automotive Radar (77 GHz):</b> Radar systems penetrate dense fog and rain with minimal electromagnetic attenuation. "
        "However, radar lacks semantic and spatial resolution. Radar cannot detect lane divider lines, cannot perceive roadway boundaries, cannot classify "
        "pedestrians reliably against metallic background clutter, and cannot identify asphalt surface craters, debris, or potholes.",
        styles['BulletItem']
    ))
    f.append(Paragraph(
        "<b>3. Standard Monocular CMOS Dashcams:</b> Standard automotive forward-facing RGB cameras are the most economically viable sensor, already installed "
        "in millions of modern vehicles. However, standard camera hardware has a fixed dynamic range. When dense fog or blinding high-beam glare enters the optical "
        "pathway, the camera's analog-to-digital converter (ADC) saturates, resulting in complete information loss (contrast wash-out or pure white blooming).",
        styles['BulletItem']
    ))
    f.append(Paragraph(
        "<b>4. Luxury OEM Thermal Cameras:</b> Far-Infrared (FIR / LWIR) thermal cameras (such as those offered on top-tier Mercedes-Benz S-Class or Audi A8 luxury "
        "packages) operate in the 8–14 μm band and can reveal thermal signatures of living pedestrians in darkness. However, these systems represent optional luxury "
        "add-ons costing Rs. 3,50,000 to Rs. 5,00,000. Furthermore, thermal sensors are effectively blinded by torrential rain downpours due to surface evaporative "
        "cooling, which eliminates thermal differentials between vehicles and wet road asphalt.",
        styles['BulletItem']
    ))
    f.append(Spacer(1, 10))
    f.append(create_callout_box(
        "The Core Engineering Dilemma",
        "Over 95% of vehicles traversing dangerous Indian highways and ghat roads are economy hatchbacks, two-wheelers, auto-rickshaws, and commercial trucks. "
        "These vehicles will never be equipped with Rs. 3.5-lakh luxury sensor suites. Therefore, there exists an urgent humanitarian and engineering imperative: "
        "can life-saving, multi-threat atmospheric perception be achieved using nothing more than a standard Rs. 1,200 commercial USB dashcam and an affordable "
        "in-vehicle edge processor?",
        styles
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 13: 1.2 ATMOSPHERIC DEGRADATION & OPTICAL PHYSICS
    # =========================================================================
    f.append(Paragraph("<b>1.2 Atmospheric Degradation and Optical Physics</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "To engineer an edge algorithm capable of inverting atmospheric degradation, one must first analyze the fundamental physics governing light transport "
        "through turbid media. The degradation of outdoor vehicular imagery is mathematically modeled by Koschmieder’s Law of Atmospheric Attenuation, "
        "formulated in 1924 and generalized by McCartney in 1976:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "$$\\mathbf{I}(x) = \\mathbf{J}(x) \\cdot t(x) + \\mathbf{A} \\cdot (1 - t(x))$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "where:<br/>"
        "• <b>I(x)</b> represents the observed, degraded RGB image captured by the vehicle's forward CMOS sensor at pixel spatial coordinate $x = (u, v)$.<br/>"
        "• <b>J(x)</b> represents the true, uncorrupted scene radiance (the crystal-clear road environment that would be perceived in zero-fog conditions).<br/>"
        "• <b>A</b> is the global atmospheric airlight vector $\\mathbf{A} = [A_R, A_G, A_B]^T$, denoting the ambient environmental illumination scattered into the optical path.<br/>"
        "• <b>t(x)</b> represents the medium transmission map, which quantifies the fraction of unscattered light that reaches the camera lens without attenuation.",
        styles['AcademicBodyNoIndent']
    ))
    f.append(Spacer(1, 8))
    f.append(Paragraph(
        "The transmission map $t(x)$ decays exponentially as a function of the physical Euclidean depth $d(x)$ between the camera optical center and the road obstacle, "
        "governed by Beer-Lambert’s Law of Extinction:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "$$t(x) = e^{-\\beta(\\lambda) \\cdot d(x)}$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "where $\\beta(\\lambda)$ is the atmospheric extinction scattering coefficient. In clear weather, $\\beta \\approx 0.001\\text{ km}^{-1}$, yielding $t(x) \\approx 1.0$. "
        "However, in mountain mist or radiation fog, $\\beta$ escalates to values between $0.05\\text{ m}^{-1}$ and $0.20\\text{ m}^{-1}$. "
        "Crucially, the scattering regime in highway fog is governed by <b>Mie Scattering</b> rather than Rayleigh scattering, because the radius of aerosol water droplets "
        "($r \\in [1\\mu m, 20\\mu m]$) is comparable to or larger than the wavelength of visible light ($\\lambda \\in [400\\text{ nm}, 700\\text{ nm}]$). "
        "Consequently, Mie scattering is wavelength-independent, causing all color channels to scatter uniformly and producing the characteristic opaque milky-white veil "
        "that blinds human drivers.",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 14: 1.3 THE DRIVING QUESTION
    # =========================================================================
    f.append(Paragraph("<b>1.3 The Driving Question</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "In strict alignment with the pedagogy of Project-Based Learning (PBL), this engineering endeavor is not governed by a rigid, pre-defined software "
        "specification handed down by an instructor. Instead, it is organized around an open-ended, investigable, and deeply challenging research question "
        "formulated at the intersection of Digital Signal Processing, Computer Vision, and Embedded Machine Learning:",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 6))
    f.append(create_callout_box(
        "The Central PBL Driving Question",
        "“Can an edge-computing, physics-guided deterministic perception framework paired with lightweight asynchronous deep neural telemetry eliminate "
        "optical atmospheric degradation, blind oncoming headlight glare, and collision hazards in real-time (>30 FPS) on sub-$50 commodity edge processors, "
        "without requiring expensive sensory arrays or cloud connectivity?”",
        styles
    ))
    f.append(Spacer(1, 10))
    f.append(Paragraph(
        "To systematically investigate and answer this driving question, our research team decomposed the overarching problem into three concrete, "
        "empirically testable engineering sub-hypotheses:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "• <b>Sub-Hypothesis 1 (Algorithmic Tractability):</b> A deterministic optical pipeline based on the Dark Channel Prior (DCP) and an $O(N)$ Fast Guided Filter "
        "with spatial subsampling can achieve image restoration quality comparable to multi-gigabyte deep generative networks (such as CycleGAN or DehazeNet), "
        "while reducing frame latency from several seconds down to under 25 milliseconds on an ordinary multi-core CPU.",
        styles['BulletItem']
    ))
    f.append(Paragraph(
        "• <b>Sub-Hypothesis 2 (Multi-Hazard Photometric Inversion):</b> Specular high-beam headlight glare and pitch-black nocturnal shadows can be decoupled "
        "and balanced through non-linear luminance knee compression and localized CLAHE in the YUV/LAB color spaces, without causing color clipping or halo artifacts.",
        styles['BulletItem']
    ))
    f.append(Paragraph(
        "• <b>Sub-Hypothesis 3 (Asynchronous Decoupling for Automotive Safety):</b> Decoupling high-frequency optical display filtering (running at 35+ FPS) "
        "from deep convolutional neural object tracking (YOLOv8 running at 12–15 Hz) via atomic double-buffering can eliminate UI freezing, guarantee deterministic "
        "frame delivery, and enable real-time Time-to-Collision (TTC) calculations on resource-constrained embedded nodes.",
        styles['BulletItem']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 15: 1.4 PROJECT & PEDAGOGICAL OBJECTIVES
    # =========================================================================
    f.append(Paragraph("<b>1.4 Project and Pedagogical Objectives</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Because this work constitutes a capstone Project-Based Learning component within the Artificial Intelligence and Machine Learning curriculum, "
        "the project is evaluated on both technical engineering rigor and pedagogical student skill growth. The objectives are defined across two distinct dimensions:",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 6))

    f.append(Paragraph("<b>1.4.1 Technical Engineering Objectives</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "1. <b>To formulate and implement an $O(N)$ real-time video dehazing core</b> based on Koschmieder’s scattering model, replacing soft matting with a Fast Guided "
        "Filter and incorporating Temporal Exponential Moving Average (EMA) airlight stabilization to eliminate luminance flickering across consecutive frames.<br/>"
        "2. <b>To engineer an active anti-glare specular attenuation engine</b> that detects blinding high-beam headlight saturation (>190 luminance) and executes "
        "smooth knee-curve compression without darkening ambient road features.<br/>"
        "3. <b>To construct a 3D drivable corridor AR lane projector</b> utilizing Canny edge DSP and Probabilistic Hough line extraction, projecting glowing neon guide rails "
        "and dynamic metric distance hash marks (5m, 15m, 30m) without obscuring asphalt visibility.<br/>"
        "4. <b>To develop a road-only asphalt pothole and anomaly scanner</b> incorporating strict HSV foliage rejection ($H \\in [20, 95], S \\ge 25$) to permanently resolve "
        "the notorious 'Tree Bug' false-positive failure mode.<br/>"
        "5. <b>To build an asynchronous deep neural tracking subsystem</b> using YOLOv8 nano and monocular ground-plane pinhole geometry to compute metric distance, "
        "Time-to-Collision (TTC), and predictive +1.5s Ghost-Vision cut-in trajectories.<br/>"
        "6. <b>To integrate a 468-point 3D biometric Driver Monitoring System (DMS)</b> utilizing MediaPipe facial mesh landmarks to measure microscopic eyelid closure "
        "(Eye Aspect Ratio) and alert drowsy drivers in real time.<br/>"
        "7. <b>To deploy a zero-install, zero-cloud web-based cockpit HUD</b> capable of streaming low-latency MJPEG video and condition-aware GPS speed limits directly "
        "to in-car Android infotainment screens over local Wi-Fi.",
        styles['AcademicBodyNoIndent']
    ))
    f.append(Spacer(1, 6))

    f.append(Paragraph("<b>1.4.2 Pedagogical and Professional Learning Objectives</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "• <b>To master the design of real-time embedded systems</b> by profiling computational bottlenecks, memory bandwidth, and threading concurrency in Python and C++ primitives.<br/>"
        "• <b>To bridge theoretical mathematical physics with practical software engineering</b> by implementing optical scattering equations and linear filter coefficients from primary literature.<br/>"
        "• <b>To practice disciplined, mentor-reviewed Agile sprint cycles</b>, maintaining weekly technical progress logs, conducting formal retrospectives, and executing engineering pivots.<br/>"
        "• <b>To synthesize multidisciplinary competencies</b> across Electronics and Communication Engineering (ECE digital image processing) and Computer Science (deep learning, web servers, and distributed edge architectures).",
        styles['BulletItem']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 16: 1.5 SCOPE, BOUNDARIES, AND LIMITATIONS
    # =========================================================================
    f.append(Paragraph("<b>1.5 Scope, Boundaries, and Operational Design Domain (ODD)</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "In professional automotive safety engineering, explicitly defining the Operational Design Domain (ODD) is essential to establish the operational "
        "boundaries under which the system is verified to operate safely and effectively. This formal scoping prevents invalid operational assumptions and provides "
        "a rigorous benchmark during academic viva examinations.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 6))

    f.append(Paragraph("<b>1.5.1 In-Scope Capabilities</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "• <b>Vehicle Platforms:</b> Passenger cars (Class M1), light commercial vehicles (Class N1), multi-axle trucks, and buses equipped with an internal 12V DC power outlet.<br/>"
        "• <b>Sensor Mounting:</b> Monocular front-facing camera mounted on the vehicle windshield along the centerline, with an elevation between 1.2 and 1.6 meters above the road plane.<br/>"
        "• <b>Camera Specifications:</b> Standard rolling-shutter CMOS RGB sensors supporting resolutions of 1280x720 (720p) or 1920x1080 (1080p) at 30 frames per second, with horizontal field-of-view (FOV) between 65° and 85°.<br/>"
        "• <b>Illumination Regimes:</b> Operational across day, dusk, tunnel transitions, and unlit night roads down to 0.05 lux ambient illuminance.<br/>"
        "• <b>Environmental Scenarios:</b> Advection fog, radiation fog, orographic mountain mist, monsoon rain downpours (up to 50 mm/hr), unlit rural roads, and oncoming high-beam glare.",
        styles['BulletItem']
    ))
    f.append(Spacer(1, 6))

    f.append(Paragraph("<b>1.5.2 Explicit Operational Boundaries & Limitations</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "• <b>Advisory Level 2+ Classification:</b> ClearDrive operates strictly as an advisory, human-in-the-loop Advanced Driver Assistance System (SAE Level 2+). "
        "It provides high-visibility visual augmentations, predictive telemetry, and audible safety chimes. It does NOT directly actuate vehicle steering, throttle, "
        "or hydraulic braking servos.<br/>"
        "• <b>Flat Ground-Plane Assumption:</b> Monocular metric distance estimation relies on pinhole camera geometry assuming a locally planar road surface. "
        "Extreme vertical road gradients (such as severe crests exceeding 15% incline) introduce transient distance estimation errors of up to ±8%.<br/>"
        "• <b>Severe Whiteout / 98% Optical Attenuation:</b> In apocalyptic blizzard or thick industrial smoke conditions where optical transmission drops below "
        "$t_0 = 0.05$ (meaning less than 5% of photons reach the sensor), the signal-to-noise ratio drops below the theoretical limits of passive RGB restoration.<br/>"
        "• <b>Camera Lens Direct Occlusion:</b> Physical obstructions adhering directly to the external windshield glass (such as thick mud splatters or opaque ice) "
        "cannot be inverted through software and require physical windshield wiper activation.",
        styles['BulletItem']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 17: 1.6 REGULATORY & SAFETY COMPLIANCE FRAMEWORK
    # =========================================================================
    f.append(Paragraph("<b>1.6 Regulatory and Safety Compliance Framework</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "To ensure that ClearDrive Tech transcends an isolated academic prototype and adheres to commercial automotive engineering standards, "
        "the architecture has been designed in strict alignment with national and international vehicular regulatory frameworks:",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 6))

    f.append(Paragraph("<b>1. Automotive Industry Standard AIS-140 (MoRTH, India):</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "AIS-140 mandates intelligent transportation systems (ITS) and emergency location tracking for all commercial public service vehicles and national permit trucks. "
        "ClearDrive incorporates real-time hardware GPS telemetry, NMEA coordinate parsing, and speed monitoring compliance, providing the foundational telemetry layer "
        "stipulated by Indian transport regulations.",
        styles['AcademicBody']
    ))

    f.append(Paragraph("<b>2. Automotive Industry Standard AIS-145 (ADAS Guidelines):</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "AIS-145 outlines technical specifications for Forward Collision Warning (FCW) and Lane Departure Warning (LDW) systems in India. ClearDrive's AR lane "
        "boundary guidance, continuous distance estimation, and audible Time-to-Collision (TTC) thresholds conform directly with AIS-145 alert timing protocols.",
        styles['AcademicBody']
    ))

    f.append(Paragraph("<b>3. ISO 26262 Road Vehicles — Functional Safety:</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "While full ASIL-D certification is reserved for drive-by-wire hardware actuators, ClearDrive's edge software architecture adopts ISO 26262 ASIL-B "
        "functional safety principles. Specifically, we implemented an autonomous Zero-Freeze Watchdog thread in `app.py` that continuously monitors frame ingestion. "
        "If a video stream or camera driver stalls for more than 30 milliseconds, the watchdog intercepts the failure, flushes internal ring buffers, and re-initializes "
        "the video stream without dropping the HTTP connection or crashing the dashboard.",
        styles['AcademicBody']
    ))

    f.append(Paragraph("<b>4. UNECE WP.29 Cyber Security Regulations (R155/R156):</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "To protect vehicular networks from wireless intrusion, ClearDrive operates on an isolated, encrypted local WPA3 Wi-Fi hotspot. The mobile dashcam node "
        "transmits frames exclusively over local TLS/HTTPS (`cert.pem`, `key.pem`) on port 5001, ensuring that video frames and telemetry cannot be snooped or spoofed "
        "by rogue nodes on the roadway.",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 18: CHAPTER 1 SUMMARY & TRANSITION
    # =========================================================================
    f.append(Paragraph("<b>1.7 Chapter Summary and Document Organization</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "This chapter established the urgent real-world motivation behind ClearDrive Tech, exploring the unique failure modes of existing luxury ADAS sensor arrays "
        "in dense Indian ghat road fog, heavy monsoon rains, pitch-black rural roads, and blinding high-beam glare. We articulated the overarching PBL Driving Question, "
        "established our technical and pedagogical learning objectives, defined our Operational Design Domain (ODD), and mapped our architecture to automotive regulatory frameworks.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "The remainder of this Project-Based Learning report is systematically structured as follows:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "• <b>Chapter 2 (Literature Survey):</b> Conducts a comprehensive mathematical and algorithmic survey of prior literature across atmospheric dehazing, "
        "Retinex night vision, anti-glare filtering, lane tracking, deep object detection, and driver monitoring, concluding with a 35-paper comparative taxonomy.<br/>"
        "• <b>Chapter 3 (Project Planning and Feasibility):</b> Documents the week-by-week Agile PBL lifecycle progress log across all 12 weeks, presents the complete "
        "System Requirements Specification (SRS), and evaluates technical, economic, and operational feasibility.<br/>"
        "• <b>Chapter 4 (Iterative Design and Methodology):</b> Explores the iterative evolution of ClearDrive across three complete cycles—from the flawed Baseline (Iteration 1) "
        "to the Refinement (Iteration 2) and the final OmniVision Engine (Iteration 3)—with complete mathematical proofs.<br/>"
        "• <b>Chapter 5 (System Implementation):</b> Details the eight modular software components, presents key annotated code listings, and outlines the dual-cockpit HUD.<br/>"
        "• <b>Chapter 6 (Results and Discussion):</b> Evaluates performance across quantitative benchmarks, real-world adverse road tests, cross-platform hardware benchmarks, and failure mode ablations.<br/>"
        "• <b>Chapter 7 (Team Reflection and Learning Outcomes):</b> Features individual pedagogical reflections, team dynamics retrospectives, and direct mapping to Course Outcomes (CO1–CO6) and Program Outcomes (PO1–PO12).<br/>"
        "• <b>Chapter 8 (Conclusion and Future Scope):</b> Summarizes project achievements and outlines the roadmap toward C-V2X, LiDAR fusion, and automotive Tier-1 commercialization.",
        styles['AcademicBodyNoIndent']
    ))
    f.append(Spacer(1, 15))
    f.append(create_callout_box(
        "Key Engineering Takeaway — Chapter 1",
        "ClearDrive Tech addresses the multi-lakh automotive safety barrier by proving that physics-guided computer vision and lightweight asynchronous neural "
        "telemetry can democratize life-saving ADAS for the millions of commercial and economy vehicles traversing hazardous Indian roads.",
        styles
    ))
    f.append(PageBreak())

    return f
