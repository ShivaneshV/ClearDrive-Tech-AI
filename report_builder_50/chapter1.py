"""
Chapter 1: Introduction (Pages 2 to 6 - Exactly 5 Pages)
ClearDrive AI: Real-Time ADAS and Vision Restoration for Adverse Driving Conditions
"""

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from report_builder_50.styles import (
    USABLE_WIDTH, COLOR_PRIMARY, COLOR_SECONDARY, COLOR_BORDER,
    create_callout_box
)


def get_chapter1_flowables(styles):
    """Returns flowables for Chapter 1 (Pages 2 to 6 - Exactly 5 Pages)."""
    f = []

    # =========================================================================
    # PAGE 2: CHAPTER 1 COVER & 1.1 BACKGROUND & MOTIVATION
    # =========================================================================
    f.append(Paragraph("<b>CHAPTER 1</b>", styles['ChapterHeader']))
    f.append(Paragraph("<b>INTRODUCTION</b>", styles['DocTitle']))
    f.append(HRFlowable(width="100%", thickness=1.2, color=COLOR_PRIMARY, spaceBefore=2, spaceAfter=10))

    f.append(Paragraph("<b>1.1 Background and Real-World Motivation</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Vehicular transportation forms the vital circulatory backbone of modern economic infrastructure. "
        "However, road safety remains one of the most pressing public health and engineering crises of the twenty-first century. "
        "According to official annual reports published by the Ministry of Road Transport and Highways (MoRTH), Government of India, "
        "the country witnesses over 4,60,000 recorded road accidents annually, claiming more than 1,68,000 human lives and inflicting permanent "
        "disabling injuries on over 4,40,000 citizens. This represents a staggering economic loss of approximately 3% of national Gross Domestic Product (GDP). "
        "A disproportionately large percentage of these catastrophic fatalities occur during adverse environmental driving conditions, specifically "
        "characterized by dense aerosol fog, blinding torrential monsoon rain, pitch-black unlit rural corridors, and the blinding glare of oncoming "
        "aftermarket LED high-beam headlights.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "In developing nations such as India, geographic and climatic realities introduce acute operational hazards rarely addressed by western-centric "
        "autonomous driving systems. Across the vast Nilgiri mountain range and the Western Ghats-encompassing high-altitude highway corridors such as "
        "the Ooty Ghat Road (consisting of 36 extreme hairpin bends), the Valparai pass (40 hairpin curves), Coonoor, and Kodaikanal-dense orographic "
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
    f.append(Spacer(1, 4))
    f.append(create_callout_box(
        "Socio-Economic Impact of Adverse Weather Collisions",
        "Over 38% of fatal highway collisions on Indian national and state expressways occur under compromised atmospheric visibility. "
        "Commercial heavy freight transport and public passenger transit bear over 60% of these casualties, highlighting an urgent societal need "
        "for accessible, retrofittable in-cockpit perception augmentation.",
        styles
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 3: 1.1.1 CONTEMPORARY SENSOR SUITE DEFICITS & ECONOMIC BARRIERS
    # =========================================================================
    f.append(Paragraph("<b>1.1.1 The Failure Modes of Contemporary Automotive Sensor Suites</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "To mitigate vehicular collisions, automotive original equipment manufacturers (OEMs) have introduced Advanced Driver Assistance Systems (ADAS). "
        "However, state-of-the-art enterprise ADAS solutions rely on physical sensor suites that exhibit fundamental, catastrophic physical failure modes "
        "when exposed to adverse weather:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "• <b>Light Detection and Ranging (LiDAR):</b> While 64-beam and 128-beam mechanical and solid-state LiDAR units deliver sub-centimeter 3D spatial "
        "reconstruction in dry, clear daylight, their operational wavelengths (typically 905 nm or 1550 nm) suffer from severe backscattering when encountering "
        "suspended aerosol water droplets and heavy rain sheets. The laser pulses reflect off raindrops and fog particles rather than roadway obstacles, "
        "generating tens of thousands of phantom 'noise points' that choke clustering algorithms and cause emergency braking lockups. Furthermore, high-end "
        "automotive LiDAR rigs cost upwards of Rs. 25,00,000, making them entirely unviable for commercial fleet adoption.",
        styles['BulletItem']
    ))
    f.append(Paragraph(
        "• <b>Millimeter-Wave Automotive Radar (77 GHz):</b> Radar systems penetrate dense fog and rain with minimal electromagnetic attenuation. "
        "However, radar lacks semantic and spatial resolution. Radar cannot detect lane divider lines, cannot perceive roadway boundaries, cannot classify "
        "pedestrians reliably against metallic background clutter, and cannot identify asphalt surface craters, debris, or potholes.",
        styles['BulletItem']
    ))
    f.append(Paragraph(
        "• <b>Standard Monocular CMOS Dashcams:</b> Standard automotive forward-facing RGB cameras are the most economically viable sensor, already installed "
        "in millions of modern vehicles. However, standard camera hardware has a fixed dynamic range. When dense fog or blinding high-beam glare enters the optical "
        "pathway, the camera's analog-to-digital converter (ADC) saturates, resulting in complete information loss (contrast wash-out or pure white blooming).",
        styles['BulletItem']
    ))
    f.append(Paragraph(
        "• <b>Luxury OEM Thermal Cameras:</b> Far-Infrared (FIR / LWIR) thermal cameras operate in the 8-14 μm band and can reveal thermal signatures in darkness. "
        "However, these systems represent optional luxury add-ons costing Rs. 3,50,000 to Rs. 5,00,000. Furthermore, thermal sensors are effectively blinded by "
        "torrential rain downpours due to surface evaporative cooling, which eliminates thermal differentials between vehicles and wet road asphalt.",
        styles['BulletItem']
    ))
    f.append(Spacer(1, 4))
    f.append(create_callout_box(
        "The Core Engineering Dilemma",
        "Sensors that penetrate bad weather (Radar) lack optical and spatial resolution. Sensors that provide rich spatial resolution (LiDAR, Cameras) "
        "fail catastrophically in aerosol fog and high-beam glare. Enterprise solutions that fuse both cost more than the average Indian passenger vehicle. "
        "ClearDrive AI resolves this dilemma through pure software edge vision intelligence.",
        styles
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 4: 1.2 ATMOSPHERIC DEGRADATION & KOSCHMIEDER OPTICAL PHYSICS
    # =========================================================================
    f.append(Paragraph("<b>1.2 Atmospheric Degradation and Koschmieder Optical Physics</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Atmospheric scattering is an ill-posed inverse optical problem governed by the interaction between photons and suspended particulate matter. "
        "In a turbid atmosphere, light scattering is categorized into <b>Rayleigh scattering</b> (where particle radius $r \\ll \\lambda$, governing fine atmospheric gases) "
        "and <b>Mie scattering</b> (where particle radius $r \\approx \\lambda$, governing water droplets, fog, mist, and aerosol smog). In automotive driving scenarios, "
        "Mie scattering dominates, causing severe angular dispersion and contrast attenuation across the visible electromagnetic spectrum (400-700 nm).",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "The physical propagation of light through a scattering medium is formalized by Koschmieder's Law (1924), which expresses the observed radiance $\\mathbf{I}(x)$ at pixel coordinate $x$ as:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "$$\\mathbf{I}(x) = \\mathbf{J}(x) \\cdot t(x) + \\mathbf{A} \\cdot (1 - t(x))$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "where $\\mathbf{J}(x)$ is the true, uncorrupted scene radiance of the roadway obstacle, $\\mathbf{A}$ is the global atmospheric airlight vector (the ambient sky radiance scattered into the line of sight), "
        "and $t(x) \\in [0, 1]$ is the medium transmission map. Under homogeneous atmospheric conditions, the transmission decays exponentially with distance $d(x)$ according to Beer-Lambert's optical extinction law:",
        styles['AcademicBodyNoIndent']
    ))
    f.append(Paragraph(
        "$$t(x) = \\exp(-\\beta \\cdot d(x))$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "where $\\beta$ is the atmospheric extinction coefficient. As distance $d(x)$ increases, transmission $t(x) \\to 0$, causing direct scene radiance to vanish into atmospheric veil $\\mathbf{A}$. "
        "Because $\\mathbf{I}(x)$ is a known 3-channel RGB vector, but both $\\mathbf{J}(x)$ (3 unknowns) and $t(x)$ (1 unknown) are unknown for every single pixel, there are 4 unknowns for 3 equations. "
        "Mathematically, the inverse recovery of $\\mathbf{J}(x)$ is severely under-constrained and requires rigorous physical priors.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))
    f.append(Paragraph("<b>Optical Glare & Sensor Dynamic Range Saturation</b>", styles['SubsectionHeader']))
    f.append(Paragraph(
        "At night, oncoming high-beam LED headlights cause extreme localized photon flux exceeding 100,000 lux. Monocular automotive CMOS sensors have typical intra-scene "
        "dynamic ranges of 60-72 dB. When high-beam glare strikes the lens, charge spillover between adjacent sensor photodiode wells creates spatial blooming, wiping out all lane markings and pedestrian cues.",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 5: 1.3 DRIVING QUESTION & 1.4 PROJECT & PEDAGOGICAL OBJECTIVES
    # =========================================================================
    f.append(Paragraph("<b>1.3 The Core Driving Question</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "The engineering formulation of this Project-Based Learning endeavor is encapsulated in the following core research question:",
        styles['AcademicBody']
    ))
    f.append(create_callout_box(
        "The PBL Driving Question",
        "&quot;How can a low-cost, monocular vision platform running entirely on consumer edge hardware simultaneously restore visibility "
        "under severe atmospheric degradation (dense fog, torrential rain, pitch-black darkness, high-beam glare) and execute real-time "
        "multi-modal ADAS (object detection, metric depth, lane guidance, pothole detection, biometric driver monitoring) with deterministic "
        "latency (&lt;33ms per frame) without relying on expensive physical sensors?&quot;",
        styles
    ))
    f.append(Spacer(1, 4))

    f.append(Paragraph("<b>1.4 Project and Pedagogical Objectives</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "To systematically answer this driving question, the project established rigorous technical and pedagogical milestones:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "• <b>RO1 (Real-Time Physics Restoration):</b> Design and implement a vectorized, $O(N)$ linear-time atmospheric dehazing engine based on the Dark Channel Prior (DCP) "
        "and Fast Guided Filter, achieving &gt;30 FPS throughput on CPU hardware without halo artifacts.",
        styles['BulletItem']
    ))
    f.append(Paragraph(
        "• <b>RO2 (Zero-Light & Anti-Glare DSP):</b> Formulate a dual-domain night enhancement pipeline combining YUV Retinex/CLAHE contrast expansion with specular knee compression "
        "to restore pitch-black rural roadways and suppress oncoming LED high-beam blooming.",
        styles['BulletItem']
    ))
    f.append(Paragraph(
        "• <b>RO3 (Neural Kinematics & Monocular Telemetry):</b> Integrate a quantized YOLOv8 nano neural detector with monocular pinhole ground-plane geometry to compute real-time "
        "metric distances $Z$ and Time-to-Collision (TTC) for critical forward obstacles.",
        styles['BulletItem']
    ))
    f.append(Paragraph(
        "• <b>RO4 (Road Hazard & Biometric DMS Sentry):</b> Develop sub-millisecond AR lane boundary projection, HSV foliage-filtered pothole scanning, and a 468-point 3D facial mesh "
        "Driver Monitoring System (DMS) detecting eyelid closure (EAR) micro-sleep events.",
        styles['BulletItem']
    ))
    f.append(Paragraph(
        "• <b>RO5 (Pedagogical Alignment & Open-Source Artifact):</b> Map experimental progress to ABET/NBA Course Outcomes (CO1-CO6), validate against AIS-140/145 guidelines, "
        "and open-source the complete codebase under the MIT license.",
        styles['BulletItem']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 6: 1.5 ODD, ASSUMPTIONS & 1.6 REGULATORY FRAMEWORK
    # =========================================================================
    f.append(Paragraph("<b>1.5 Operational Design Domain (ODD), Boundaries, and Assumptions</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "To establish rigorous engineering constraints, the Operational Design Domain (ODD) of ClearDrive AI is defined as follows:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "• <b>Vehicle Dynamic Range:</b> Operational vehicle speeds from 0 km/h (stationary queue) up to 120 km/h (expressway cruising).<br/>"
        "• <b>Atmospheric Boundaries:</b> Radiation and advection fog down to 10 m meteorological visibility; monsoon rainfall up to 50 mm/h; ambient illumination from 0.05 lux (starlight rural) to 100,000 lux (direct sun / high-beam glare).<br/>"
        "• <b>Sensor Assumptions:</b> Monocular forward-facing RGB CMOS camera (720p/1080p, 30 FPS, FOV 90°-120°) mounted along the windshield centerline; inward-facing 720p DMS camera; 100% offline edge processing.",
        styles['BulletItem']
    ))
    f.append(Spacer(1, 4))

    f.append(Paragraph("<b>1.6 Regulatory Compliance and Automotive Safety Framework</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "ClearDrive AI is designed in strict conformance with Indian and international automotive safety and functional safety standards:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "• <b>Automotive Industry Standard AIS-140:</b> Specifies Intelligent Transportation System (ITS) requirements for public and commercial vehicles in India. "
        "ClearDrive AI adheres to AIS-140 emergency response protocols, GPS telematics logging formats, and real-time health broadcast telemetry.",
        styles['BulletItem']
    ))
    f.append(Paragraph(
        "• <b>Automotive Industry Standard AIS-145:</b> Formulates guidelines for Advanced Driver Assistance Systems (ADAS), including Forward Collision Warning (FCW) "
        "and Lane Departure Warning (LDW). ClearDrive AI's TTC warning tiers (&lt;1.8s critical, &lt;2.8s advisory) directly satisfy AIS-145 acoustic and visual alert thresholds.",
        styles['BulletItem']
    ))
    f.append(Paragraph(
        "• <b>ISO 26262 ASIL-B Alignment:</b> Implements silent advisory fail-safe operation. The system acts strictly as an advisory cockpit overlay; software exceptions "
        "trigger immediate graceful degradation to raw camera bypass within 15 ms, completely preventing control hijacking or driver distraction.",
        styles['BulletItem']
    ))
    f.append(Paragraph(
        "• <b>UNECE WP.29 Cyber Security Compliance:</b> Complete 100% local edge processing with zero cloud telemetry streaming guarantees zero surface area "
        "for remote vehicular hijacking, adhering to UNECE WP.29 vehicle cybersecurity mandates.",
        styles['BulletItem']
    ))
    f.append(PageBreak())

    return f
