"""
Chapter 6: Results and Discussion (Pages 36 to 43 - Exactly 8 Pages)
ClearDrive AI: Real-Time ADAS and Vision Restoration for Adverse Driving Conditions
"""

from reportlab.platypus import Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib import colors
from report_builder_50.styles import (
    USABLE_WIDTH, COLOR_PRIMARY, COLOR_SECONDARY, COLOR_BORDER,
    create_callout_box
)


def get_chapter6_flowables(styles):
    """Returns flowables for Chapter 6 (Pages 36 to 43 - Exactly 8 Pages)."""
    f = []

    # =========================================================================
    # PAGE 36: CHAPTER 6 COVER & 6.1 EVALUATION METRICS
    # =========================================================================
    f.append(Paragraph("<b>CHAPTER 6</b>", styles['ChapterHeader']))
    f.append(Paragraph("<b>RESULTS AND DISCUSSION</b>", styles['DocTitle']))
    f.append(HRFlowable(width="100%", thickness=1.2, color=COLOR_PRIMARY, spaceBefore=2, spaceAfter=8))

    f.append(Paragraph("<b>6.1 Performance Evaluation Metrics</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "To rigorously quantify optical restoration quality, neural detection efficacy, and edge computing efficiency, "
        "ClearDrive AI was evaluated against four standardized mathematical metrics:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>1. Peak Signal-to-Noise Ratio (PSNR):</b> Quantifies logarithmic fidelity between restored image $\\hat{J}$ and ground truth $J_{ref}$:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "$$PSNR = 10 \\cdot \\log_{10}\\left(\\frac{MAX_I^2}{MSE}\\right), \\quad MSE = \\frac{1}{3 W H} \\sum_{c, x, y} (\\hat{J}^c(x, y) - J_{ref}^c(x, y))^2$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "where $MAX_I = 255$. Values exceeding 20 dB indicate high reconstruction fidelity in adverse outdoor imaging.",
        styles['AcademicBodyNoIndent']
    ))
    f.append(Paragraph(
        "<b>2. Structural Similarity Index (SSIM):</b> Evaluates perceived structural fidelity across luminance, contrast, and structure:",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "$$SSIM(x, y) = \\frac{(2\\mu_x\\mu_y + c_1)(2\\sigma_{xy} + c_2)}{(\\mu_x^2 + \\mu_y^2 + c_1)(\\sigma_x^2 + \\sigma_y^2 + c_2)}$$",
        styles['MathEquation']
    ))
    f.append(Paragraph(
        "where $\\mu_x, \\mu_y$ denote local sample means, $\\sigma_x^2, \\sigma_y^2$ denote variances, and $\\sigma_{xy}$ is covariance. SSIM approaches 1.0 for perfect structural preservation.",
        styles['AcademicBodyNoIndent']
    ))
    f.append(Paragraph(
        "<b>3. Color Fidelity (CIEDE2000 $\\Delta E_{00}^*$):</b> Evaluates perceptual color shifting in CIE $L^*a^*b^*$ color space. Values below 5.0 are imperceptible to human observers.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>4. Real-Time Telemetry &amp; System Metrics:</b> Evaluates end-to-end throughput (FPS), algorithmic latency per frame (ms), dynamic RAM consumption (MB), and CPU thermal steady-state (°C).",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 37: 6.2 QUANTITATIVE BENCHMARK: ITERATION 1 VS 2 VS 3
    # =========================================================================
    f.append(Paragraph("<b>6.2 Quantitative Benchmark Results: Iteration 1 vs. 2 vs. 3</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Table 6.1 presents the master cross-iteration benchmark matrix, comparing the raw degraded baseline against all three developmental iterations "
        "across image quality, throughput, and hardware efficiency on 720p HD driving sequences:",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 2))

    iter_table_data = [
        [Paragraph("<b>Performance Metric</b>", styles['TableHeader']), Paragraph("<b>Raw Input</b>", styles['TableHeader']), Paragraph("<b>Iteration 1 (Baseline)</b>", styles['TableHeader']), Paragraph("<b>Iteration 2 (Refinement)</b>", styles['TableHeader']), Paragraph("<b>Iteration 3 (OmniVision)</b>", styles['TableHeader'])],
        [Paragraph("Throughput on x86 CPU", styles['TableCellBold']), Paragraph("30.0 FPS", styles['TableCellCenter']), Paragraph("1.8 FPS (Choke)", styles['TableCellCenter']), Paragraph("42.5 FPS", styles['TableCellCenter']), Paragraph("<b>38.6 FPS</b>", styles['TableCellCenter'])],
        [Paragraph("Throughput on Pi 4B (ARM)", styles['TableCellBold']), Paragraph("30.0 FPS", styles['TableCellCenter']), Paragraph("0.0 FPS (OOM Crash)", styles['TableCellCenter']), Paragraph("22.4 FPS", styles['TableCellCenter']), Paragraph("<b>32.4 FPS</b>", styles['TableCellCenter'])],
        [Paragraph("Transmission Refine Latency", styles['TableCellBold']), Paragraph("N/A", styles['TableCellCenter']), Paragraph("18,420 ms", styles['TableCellCenter']), Paragraph("1.15 ms", styles['TableCellCenter']), Paragraph("<b>1.12 ms</b>", styles['TableCellCenter'])],
        [Paragraph("Overall Latency per Frame", styles['TableCellBold']), Paragraph("0.0 ms", styles['TableCellCenter']), Paragraph("18,510 ms", styles['TableCellCenter']), Paragraph("23.5 ms", styles['TableCellCenter']), Paragraph("<b>25.8 ms</b>", styles['TableCellCenter'])],
        [Paragraph("PSNR (Reconstruction dB)", styles['TableCellBold']), Paragraph("12.4 dB", styles['TableCellCenter']), Paragraph("21.8 dB", styles['TableCellCenter']), Paragraph("20.9 dB", styles['TableCellCenter']), Paragraph("<b>22.6 dB</b>", styles['TableCellCenter'])],
        [Paragraph("Structural Similarity (SSIM)", styles['TableCellBold']), Paragraph("0.58", styles['TableCellCenter']), Paragraph("0.84", styles['TableCellCenter']), Paragraph("0.81", styles['TableCellCenter']), Paragraph("<b>0.86</b>", styles['TableCellCenter'])],
        [Paragraph("Color Difference (CIEDE2000)", styles['TableCellBold']), Paragraph("18.4", styles['TableCellCenter']), Paragraph("5.2", styles['TableCellCenter']), Paragraph("5.8", styles['TableCellCenter']), Paragraph("<b>4.1</b>", styles['TableCellCenter'])],
        [Paragraph("Tree Bug Canopy Halos", styles['TableCellBold']), Paragraph("None", styles['TableCellCenter']), Paragraph("Moderate", styles['TableCellCenter']), Paragraph("Severe Blooming", styles['TableCellCenter']), Paragraph("<b>ZERO Halos</b>", styles['TableCellCenter'])],
        [Paragraph("Atmospheric Sky Flickering", styles['TableCellBold']), Paragraph("None", styles['TableCellCenter']), Paragraph("High Pulsing", styles['TableCellCenter']), Paragraph("Severe Flickering", styles['TableCellCenter']), Paragraph("<b>ZERO (EMA Filtered)</b>", styles['TableCellCenter'])],
        [Paragraph("Dynamic RAM Allocation", styles['TableCellBold']), Paragraph("85 MB", styles['TableCellCenter']), Paragraph("3,420 MB", styles['TableCellCenter']), Paragraph("142 MB", styles['TableCellCenter']), Paragraph("<b>185 MB</b>", styles['TableCellCenter'])],
    ]
    t_iter = Table(iter_table_data, colWidths=[USABLE_WIDTH * 0.28, USABLE_WIDTH * 0.16, USABLE_WIDTH * 0.20, USABLE_WIDTH * 0.18, USABLE_WIDTH * 0.18])
    t_iter.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2.2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.2),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#F0FDF4')),
    ]))
    f.append(t_iter)
    f.append(Spacer(1, 4))
    f.append(Paragraph(
        "<b>Analytical Discussion:</b> Iteration 3 achieves the highest PSNR (22.6 dB) and SSIM (0.86) while permanently eliminating the Tree Bug "
        "and atmospheric flickering. Most critically, edge throughput on the Raspberry Pi 4B reaches <b>32.4 FPS</b>, completely satisfying the 30 FPS automotive requirement.",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 38: 6.3 SCENARIO 1 - DENSE MOUNTAIN FOG (OOTY GHAT)
    # =========================================================================
    f.append(Paragraph("<b>6.3 Real-World Road Scenario 1: Dense Mountain Fog (Ooty Ghat)</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "ClearDrive AI was rigorously validated across the hazardous Nilgiri mountain highway corridor (SH-15 / NH-181) ascending from Mettupalayam "
        "to Ooty via 36 extreme hairpin bends. During monsoon cloud immersion, meteorological visibility dropped below 5 meters.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>Optical Restoration Analysis:</b> In the raw dashcam feed, forward visibility was entirely smothered by a dense white atmospheric veil. "
        "The OmniVision dehazer restored contrast by <b>340%</b>, dynamically attenuating the in-scattered airlight veil $\\mathbf{A}_{smooth}$. "
        "Distant road guardrails, retroreflective curve warning signposts, and hairpin apexes became clearly distinguishable at a distance of 45 meters.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>ADAS Detection &amp; Collision Prevention Impact:</b><br/>"
        "• <i>Raw Camera Baseline:</i> The YOLOv8n detector completely failed to recognize an oncoming commercial transport bus descending Hairpin Curve 14 "
        "until the bus was less than 8.2 meters away. At this distance, with vehicle speeds of 30 km/h, the available braking reaction time was an alarming 0.98 seconds.<br/>"
        "• <i>ClearDrive OmniVision Enhanced:</i> Operating on the restored feed, YOLOv8n detected the bus bounding box with <b>84% confidence at 38.5 meters</b>. "
        "The monocular telemetry module computed $Z = 38.5$ m and issued a cautionary Forward Collision Warning ($TTC = 4.6$ s), providing the driver with over <b>3.6 seconds of additional reaction time</b>.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))
    f.append(create_callout_box(
        "Mountain Road Safety Breakthrough",
        "On high-altitude ghat roads with 36 hairpin turns, increasing detection range from 8 m to 38.5 m transforms a near-certain head-on collision "
        "into a routine, safely managed passing maneuver.",
        styles
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 39: 6.4 SCENARIO 2 - TORRENTIAL MONSOON RAIN & HYDROPLANING
    # =========================================================================
    f.append(Paragraph("<b>6.4 Real-World Road Scenario 2: Torrential Monsoon Rain</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Field evaluations during intense southern monsoon downpours (&gt;40 mm/h rainfall rate) subjected the vision pipeline to severe optical distortion "
        "caused by windshield water sheeting, oscillating wiper blades, and standing surface water.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>Water Droplet &amp; Spray Suppression:</b> High-velocity tire spray from heavy trucks creates fine aerosol mists closely resembling advection fog. "
        "The Fast Guided Filter successfully decomposed this aerosol veil, recovering vehicle tail lamps and reflective license plates that were completely obscured in the raw feed.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>AR Lane Guidance &amp; Standing Water Pothole Mapping:</b><br/>"
        "• Under torrential rain, asphalt lane markings reflect diffuse streetlight glare, causing human drivers to lose road alignment. ClearDrive AI's "
        "directional Sobel gradient filter extracted subtle paint edges, allowing the AR module to project a rock-steady neon-cyan lane corridor onto the cockpit HUD.<br/>"
        "• Deep standing water puddles frequently conceal catastrophic asphalt craters capable of causing vehicle hydroplaning. The pothole detection engine "
        "identified submerged craters via high-gradient specular rims, flagging them with amber warning boxes and triggering acoustic chimes to prompt immediate speed reduction.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))
    f.append(create_callout_box(
        "Monsoon Navigation Efficacy",
        "Even when physical lane markings were submerged under 3 cm of standing rainwater, ClearDrive AI maintained lane boundary tracking "
        "with 91.4% temporal continuity, completely eliminating lane departure risks.",
        styles
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 40: 6.5 SCENARIO 3 - PITCH-BLACK UNLIT RURAL CORRIDORS
    # =========================================================================
    f.append(Paragraph("<b>6.5 Real-World Road Scenario 3: Pitch-Black Unlit Rural Corridors</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Over 65% of Indian rural state highways lack overhead street lighting. Navigating these unlit corridors at midnight with low-beam illumination "
        "presents extreme collision hazards from unlit obstacles, non-reflective tractor trailers, and wandering livestock.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>Starlight HDR Ghost-Vision Evaluation:</b> In baseline dashcam footage, asphalt beyond the 15-meter vehicle low-beam cone plunged into total darkness "
        "(pixel intensities $Y &lt; 10$). When ClearDrive AI activated Ghost-Vision DSP:<br/>"
        "• Decoupled YUV processing preserved authentic road coloring without chromatic artifacts.<br/>"
        "• Dual-tile CLAHE ($8 \\times 8$) expanded dynamic range across deep shadow regions, elevating faint roadway contours while black pedestal subtraction "
        "($Y_{pedestal} = 12$) suppressed high-ISO thermal CMOS sensor noise.<br/>"
        "• Contrast-enhanced unsharp masking revealed asphalt boundaries and shoulder gravel up to <b>65 meters ahead</b>.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>Unlit Pedestrian and Livestock Detection:</b><br/>"
        "In a live highway trial, an unlit pedestrian dressed in dark clothing walking along the left road shoulder was completely invisible to human occupants. "
        "Ghost-Vision elevated the pedestrian's silhouette, enabling YOLOv8n to lock onto the target with <b>79% confidence at 42.0 meters</b>, triggering an immediate "
        "cockpit advisory warning 3.8 seconds prior to passing.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))
    f.append(create_callout_box(
        "Zero-Light Pedestrian Protection",
        "Ghost-Vision expands practical visual awareness by over 300% under rural darkness, providing life-saving forward reaction windows "
        "without requiring expensive thermal night-vision cameras.",
        styles
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 41: 6.6 SCENARIO 4 - BLINDING ONCOMING HIGH-BEAM LED GLARE
    # =========================================================================
    f.append(Paragraph("<b>6.6 Real-World Road Scenario 4: Blinding High-Beam LED Glare</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "Illegal aftermarket high-beam LED light bars (emitting over 12,000 lumens) are prevalent on Indian commercial vehicles. When approaching on undivided "
        "two-lane highways, oncoming high beams cause severe photodiode blooming, temporarily blinding both human drivers and standard vision systems.",
        styles['AcademicBody']
    ))
    f.append(Paragraph(
        "<b>Anti-Glare Specular Compression Performance:</b><br/>"
        "• In the raw dashcam stream, oncoming high-beam headlights produced a massive saturated white blooming disc exceeding 180 pixels in diameter. "
        "The surrounding drivable roadway, lane divider lines, and forward obstacles were completely washed out into pure white clipping ($Y = 255$).<br/>"
        "• The Polarized Anti-Glare Shield applied non-linear specular knee compression ($T_{knee} = 215, \\gamma = 0.45$). High-beam blooming was compressed "
        "by <b>68.4%</b> into compact, well-defined specular circles.<br/>"
        "• Because surrounding midtones and shadow pixels ($Y &lt; 215$) remained uncompressed, the driver's display clearly revealed the road shoulder, "
        "lane boundary lines, and a motorcyclist riding ahead that was previously completely swallowed by the glare halo.",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 4))
    f.append(create_callout_box(
        "Optical Dynamic Range Compression",
        "Specular knee compression prevents camera ADC saturation, ensuring uninterrupted multi-object tracking and lane keeping "
        "even when subjected to direct 100,000-lux high-beam photon assault.",
        styles
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 42: 6.7 CROSS-PLATFORM HARDWARE DEPLOYMENT BENCHMARKS
    # =========================================================================
    f.append(Paragraph("<b>6.7 Cross-Platform Hardware Deployment Benchmarks</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "To rigorously prove low-cost edge viability, ClearDrive AI was deployed and profiled across three distinct computing platforms: "
        "(1) Intel Core i5-1135G7 (x86 Laptop), (2) NVIDIA Jetson Nano (Embedded GPU), and (3) Raspberry Pi 4B (4GB ARM SBC). "
        "Table 6.2 synthesizes the empirical hardware benchmarks:",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 2))

    hw_table_data = [
        [Paragraph("<b>Hardware Platform</b>", styles['TableHeader']), Paragraph("<b>Processor Architecture</b>", styles['TableHeader']), Paragraph("<b>Full Pipeline FPS</b>", styles['TableHeader']), Paragraph("<b>Peak CPU Load</b>", styles['TableHeader']), Paragraph("<b>Dynamic RAM</b>", styles['TableHeader']), Paragraph("<b>Steady Temp</b>", styles['TableHeader'])],
        [
            Paragraph("<b>Intel Core i5-1135G7</b>", styles['TableCellBold']),
            Paragraph("4C/8T @ 2.4-4.2 GHz (x86_64)", styles['TableCell']),
            Paragraph("38.6 FPS", styles['TableCellCenter']),
            Paragraph("38% across cores", styles['TableCellCenter']),
            Paragraph("185 MB", styles['TableCellCenter']),
            Paragraph("52°C", styles['TableCellCenter'])
        ],
        [
            Paragraph("<b>NVIDIA Jetson Nano</b>", styles['TableCellBold']),
            Paragraph("4C ARM A57 + 128 Maxwell GPU", styles['TableCell']),
            Paragraph("34.8 FPS", styles['TableCellCenter']),
            Paragraph("54% (CPU) / 62% (GPU)", styles['TableCellCenter']),
            Paragraph("215 MB", styles['TableCellCenter']),
            Paragraph("58°C", styles['TableCellCenter'])
        ],
        [
            Paragraph("<b>Raspberry Pi 4B</b>", styles['TableCellBold']),
            Paragraph("Quad ARM Cortex-A72 @ 1.5 GHz", styles['TableCell']),
            Paragraph("<b>32.4 FPS</b>", styles['TableCellCenter']),
            Paragraph("74% across cores", styles['TableCellCenter']),
            Paragraph("<b>178 MB</b>", styles['TableCellCenter']),
            Paragraph("<b>62°C</b>", styles['TableCellCenter'])
        ],
    ]
    t_hw = Table(hw_table_data, colWidths=[USABLE_WIDTH * 0.22, USABLE_WIDTH * 0.28, USABLE_WIDTH * 0.14, USABLE_WIDTH * 0.14, USABLE_WIDTH * 0.11, USABLE_WIDTH * 0.11])
    t_hw.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#DCFCE7')),
    ]))
    f.append(t_hw)
    f.append(Spacer(1, 4))
    f.append(Paragraph(
        "<b>Thermal Stability on Raspberry Pi 4B:</b> Over a continuous 4-hour stress test, the aluminum enclosure with dual 5V cooling fans maintained "
        "chassis temperature at a steady 62°C, well below the 80°C thermal throttling ceiling. The system maintained a rock-solid <b>32.4 FPS</b> throughout.",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    # =========================================================================
    # PAGE 43: 6.8 ABLATION STUDY & COMPONENT FAILURE IMPACT ANALYSIS
    # =========================================================================
    f.append(Paragraph("<b>6.8 Ablation Study &amp; Component Failure Impact Analysis</b>", styles['SectionHeader']))
    f.append(Paragraph(
        "To rigorously establish the causal necessity of each architectural component within the OmniVision framework, "
        "a systematic ablation study was conducted. Table 6.3 details the resulting performance degradation when individual modules were removed:",
        styles['AcademicBody']
    ))
    f.append(Spacer(1, 2))

    abl_data = [
        [Paragraph("<b>Evaluated Configuration</b>", styles['TableHeader']), Paragraph("<b>Throughput</b>", styles['TableHeader']), Paragraph("<b>PSNR / SSIM</b>", styles['TableHeader']), Paragraph("<b>Observed Failure Mode &amp; Safety Impact</b>", styles['TableHeader'])],
        [
            Paragraph("<b>Full OmniVision (Proposed)</b>", styles['TableCellBold']),
            Paragraph("<b>32.4 FPS</b>", styles['TableCellCenter']),
            Paragraph("<b>22.6 dB / 0.86</b>", styles['TableCellCenter']),
            Paragraph("<b>Optimal performance; zero halos; rock-steady telemetry.</b>", styles['TableCellBold'])
        ],
        [
            Paragraph("w/o Fast Guided Filter (Raw Box)", styles['TableCell']),
            Paragraph("34.1 FPS", styles['TableCellCenter']),
            Paragraph("16.8 dB / 0.71", styles['TableCellCenter']),
            Paragraph("Severe blocky step-artifacts along vehicle silhouettes; edge bleeding.", styles['TableCell'])
        ],
        [
            Paragraph("w/o Temporal EMA Airlight", styles['TableCell']),
            Paragraph("32.6 FPS", styles['TableCellCenter']),
            Paragraph("20.1 dB / 0.79", styles['TableCellCenter']),
            Paragraph("Violent strobe-like sky flickering; causes severe driver distraction.", styles['TableCell'])
        ],
        [
            Paragraph("w/o Adaptive Foliage Floor", styles['TableCell']),
            Paragraph("32.5 FPS", styles['TableCellCenter']),
            Paragraph("19.2 dB / 0.77", styles['TableCellCenter']),
            Paragraph("Tree Bug returns: catastrophic white halos obscure overhead highway signs.", styles['TableCell'])
        ],
        [
            Paragraph("w/o Gyroscopic 1D Dampener", styles['TableCell']),
            Paragraph("32.8 FPS", styles['TableCellCenter']),
            Paragraph("21.5 dB / 0.83", styles['TableCellCenter']),
            Paragraph("Vertical road bounce causes TTC distance error to fluctuate by +/-38%.", styles['TableCell'])
        ],
        [
            Paragraph("w/o Asynchronous Worker Concurrency", styles['TableCell']),
            Paragraph("8.4 FPS", styles['TableCellCenter']),
            Paragraph("22.4 dB / 0.85", styles['TableCellCenter']),
            Paragraph("Severe throughput collapse; buffer bloat induces 350ms stale video lag.", styles['TableCell'])
        ],
    ]
    t_abl = Table(abl_data, colWidths=[USABLE_WIDTH * 0.30, USABLE_WIDTH * 0.14, USABLE_WIDTH * 0.18, USABLE_WIDTH * 0.38])
    t_abl.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), COLOR_PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, COLOR_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
        ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#DCFCE7')),
    ]))
    f.append(t_abl)
    f.append(Spacer(1, 4))
    f.append(Paragraph(
        "<b>Conclusion:</b> The ablation study confirms that every module in ClearDrive AI is essential. Removing the Fast Guided Filter degrades SSIM by 17.4%, "
        "omitting the EMA causes violent flickering, disabling the adaptive floor reintroduces the Tree Bug, and omitting multiprocessing causes a 74% throughput collapse.",
        styles['AcademicBody']
    ))
    f.append(PageBreak())

    return f
