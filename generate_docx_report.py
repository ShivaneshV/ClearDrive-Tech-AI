"""
ClearDrive AI: 55-Page Academic Project-Based Learning (PBL) Report
Native Microsoft Word (.docx) Document Generator
Chennai Institute of Technology (Autonomous) | Department of AI & ML
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

DOCX_FILENAME = "ClearDrive_AI_55_Page_PBL_Report.docx"

# Color Palette
COLOR_NAVY_HEX = "0F2A4A"
COLOR_BLUE_HEX = "1E56A0"
COLOR_LIGHT_BG_HEX = "F1F5F9"
COLOR_CALLOUT_BG_HEX = "F0F9FF"
COLOR_BORDER_HEX = "CBD5E1"
COLOR_ACCENT_HEX = "0284C7"

COLOR_NAVY = RGBColor(15, 42, 74)
COLOR_BLUE = RGBColor(30, 86, 160)
COLOR_DARK = RGBColor(26, 26, 26)
COLOR_MUTED = RGBColor(75, 85, 99)


def set_cell_background(cell, hex_color):
    """Sets background shading of a table cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    tcPr.append(shd)


def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Sets internal padding for a table cell in dxa (1 pt = 20 dxa)."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)


def set_table_borders(table, color="CBD5E1", sz="4", val="single"):
    """Applies clean borders to a table."""
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'  <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:left w:val="none"/>'
        f'  <w:right w:val="none"/>'
        f'  <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'  <w:insideV w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)


def add_code_block(doc, code_text):
    """Creates a shaded monospace code box."""
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    cell = t.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, COLOR_LIGHT_BG_HEX)
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    
    # Border
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="4" w:color="{COLOR_BORDER_HEX}"/>'
        f'  <w:bottom w:val="single" w:sz="4" w:color="{COLOR_BORDER_HEX}"/>'
        f'  <w:left w:val="single" w:sz="12" w:color="{COLOR_BLUE_HEX}"/>'
        f'  <w:right w:val="single" w:sz="4" w:color="{COLOR_BORDER_HEX}"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(code_text)
    run.font.name = "Consolas"
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(30, 41, 59)
    doc.add_paragraph()  # spacer


def add_callout(doc, title, body):
    """Creates a stylized academic callout box."""
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    cell = t.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, COLOR_CALLOUT_BG_HEX)
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
    
    # Left border only
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'  <w:top w:val="none"/>'
        f'  <w:bottom w:val="none"/>'
        f'  <w:left w:val="single" w:sz="18" w:color="{COLOR_ACCENT_HEX}"/>'
        f'  <w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(3)
    run_t = p.add_run(title + "\n")
    run_t.bold = True
    run_t.font.name = "Arial"
    run_t.font.size = Pt(10)
    run_t.font.color.rgb = COLOR_NAVY
    
    run_b = p.add_run(body)
    run_b.italic = True
    run_b.font.name = "Times New Roman"
    run_b.font.size = Pt(9.5)
    run_b.font.color.rgb = COLOR_DARK
    doc.add_paragraph()  # spacer


def add_figure_image(doc, fig_path, fig_caption, width_inches=5.8):
    """Inserts a high-resolution figure image centered with a styled academic caption."""
    if os.path.exists(fig_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(4)
        run_img = p_img.add_run()
        run_img.add_picture(fig_path, width=Inches(width_inches))

        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(10)
        run_cap = p_cap.add_run(fig_caption)
        run_cap.bold = True
        run_cap.font.name = "Arial"
        run_cap.font.size = Pt(9)
        run_cap.font.color.rgb = COLOR_NAVY
    else:
        # Fallback to callout if image missing
        add_callout(doc, fig_caption, f"[Image: {fig_path}]")


def build_word_document():
    print("=" * 70)
    print("GENERATING CLEARDRIVE AI 55-PAGE NATIVE WORD (.DOCX) REPORT")
    print("=" * 70)

    doc = docx.Document()

    # Page Setup (A4 with 0.75" left, 0.62" right, 0.7" top/bottom)
    section = doc.sections[0]
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    section.top_margin = Inches(0.7)
    section.bottom_margin = Inches(0.7)
    section.left_margin = Inches(0.75)
    section.right_margin = Inches(0.62)

    # Header and Footer
    header = section.header
    hp = header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hrun = hp.add_run("CHENNAI INSTITUTE OF TECHNOLOGY  |  DEPT. OF AI & ML  |  CLEARDRIVE AI")
    hrun.font.name = "Arial"
    hrun.font.size = Pt(8)
    hrun.font.color.rgb = COLOR_MUTED

    footer = section.footer
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    frun = fp.add_run("B.E. (AI & ML) - Project-Based Learning Report  |  ClearDrive AI")
    frun.font.name = "Arial"
    frun.font.size = Pt(8)
    frun.font.color.rgb = COLOR_MUTED

    # Configure Normal Style
    style_normal = doc.styles['Normal']
    style_normal.font.name = 'Times New Roman'
    style_normal.font.size = Pt(10.5)
    style_normal.font.color.rgb = COLOR_DARK
    style_normal.paragraph_format.line_spacing = 1.15
    style_normal.paragraph_format.space_after = Pt(4)

    # Configure Headings
    h1_style = doc.styles['Heading 1']
    h1_style.font.name = 'Arial'
    h1_style.font.size = Pt(15)
    h1_style.font.bold = True
    h1_style.font.color.rgb = COLOR_NAVY
    h1_style.paragraph_format.space_before = Pt(14)
    h1_style.paragraph_format.space_after = Pt(4)
    h1_style.paragraph_format.keep_with_next = True

    h2_style = doc.styles['Heading 2']
    h2_style.font.name = 'Arial'
    h2_style.font.size = Pt(12)
    h2_style.font.bold = True
    h2_style.font.color.rgb = COLOR_BLUE
    h2_style.paragraph_format.space_before = Pt(10)
    h2_style.paragraph_format.space_after = Pt(3)
    h2_style.paragraph_format.keep_with_next = True

    h3_style = doc.styles['Heading 3']
    h3_style.font.name = 'Arial'
    h3_style.font.size = Pt(10.5)
    h3_style.font.bold = True
    h3_style.font.color.rgb = COLOR_NAVY
    h3_style.paragraph_format.space_before = Pt(6)
    h3_style.paragraph_format.space_after = Pt(2)
    h3_style.paragraph_format.keep_with_next = True

    # =========================================================================
    # PAGE 1: TITLE PAGE & BONAFIDE CERTIFICATE
    # =========================================================================
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("CLEARDRIVE AI: REAL-TIME ADAS AND VISION RESTORATION FOR ADVERSE DRIVING CONDITIONS\n")
    r.bold = True
    r.font.size = Pt(15)
    r.font.name = "Arial"
    r.font.color.rgb = COLOR_NAVY

    r = p.add_run("A PROJECT BASED LEARNING REPORT\n")
    r.bold = True
    r.font.size = Pt(11)
    r.font.name = "Arial"
    r.font.color.rgb = COLOR_BLUE

    r = p.add_run("Submitted in partial fulfilment of the requirements for the\nProject Based Learning component of Machine Learning\nBACHELOR OF ENGINEERING in ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING\n\n")
    r.font.size = Pt(9.5)

    r = p.add_run("Submitted by:\n")
    r.bold = True
    r.font.size = Pt(10)
    r = p.add_run("SHIVANESH V [Reg. No. 210425148109]\nVISHNU PRASATH S [Reg. No. 210425148134]\n\n")
    r.font.size = Pt(10)

    r = p.add_run("CHENNAI INSTITUTE OF TECHNOLOGY, CHENNAI - 600069\n")
    r.bold = True
    r.font.size = Pt(11)
    r.font.name = "Arial"
    r.font.color.rgb = COLOR_NAVY
    r = p.add_run("(An Autonomous Institution Affiliated to Anna University, Chennai)\nOCTOBER 2026\n\n")
    r.font.size = Pt(9.5)

    doc.add_page_break()

    # =========================================================================
    # INSTITUTIONAL & DEPARTMENTAL VISION & MISSION
    # =========================================================================
    doc.add_heading("CHENNAI INSTITUTE OF TECHNOLOGY, CHENNAI", level=1)
    p = doc.add_paragraph("(An Autonomous Institution Affiliated to Anna University, Chennai)")
    p.runs[0].italic = True

    doc.add_heading("Vision of the Institute", level=2)
    p = doc.add_paragraph(
        "To be an eminent centre for academia, industry, and research by imparting knowledge, "
        "relevant practices, and innovative thinking to foster globally responsible and competent engineers."
    )
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    doc.add_heading("Mission of the Institute", level=2)
    doc.add_paragraph("• M1: To create a conducive learning environment that promotes innovation, research, and entrepreneurship.")
    doc.add_paragraph("• M2: To collaborate with industries and academia to bridge the gap between curriculum and industry requirements.")
    doc.add_paragraph("• M3: To instill high standards of professional ethics, human values, and social responsibilities in all engineering domains.")
    doc.add_paragraph("• M4: To contribute towards the research ecosystem by providing a suitable infrastructure and incubation environment.")

    doc.add_heading("DEPARTMENT OF ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING", level=1)
    doc.add_heading("Vision of the Department", level=2)
    p = doc.add_paragraph(
        "“Developing skilled AI and ML professionals empowered through research and innovation to address global challenges and to enhance societal well-being.”\n"
        "To excel in Artificial Intelligence and Machine Learning education and research, producing ethical, competent, and socially committed engineers capable of addressing real-world challenges through intelligent systems."
    )
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    doc.add_heading("Mission of the Department", level=2)
    doc.add_paragraph("• DM1: Provide comprehensive education and skill development in AI and ML, equipping students with strong engineering knowledge, modern tools, and analytical abilities to solve complex problems.")
    doc.add_paragraph("• DM2: Foster research, innovation, and design thinking to develop intelligent solutions that address real-world challenges, advance societal welfare, and drive industrial growth.")
    doc.add_paragraph("• DM3: Promote ethical, professional, and collaborative practices by nurturing teamwork, effective communication, leadership, and adherence to professional ethics.")
    doc.add_paragraph("• DM4: Encourage lifelong learning, entrepreneurship, and sustainable practices to empower graduates to contribute responsibly to society and global industries.")

    doc.add_page_break()

    # =========================================================================
    # BONAFIDE CERTIFICATE
    # =========================================================================
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("BONAFIDE CERTIFICATE\n")
    r.bold = True
    r.font.size = Pt(13)
    r.font.name = "Arial"
    r.font.color.rgb = COLOR_NAVY

    p = doc.add_paragraph(
        "This is to certify that the Project-Based Learning report titled 'CLEARDRIVE AI: REAL-TIME ADAS AND VISION RESTORATION "
        "FOR ADVERSE DRIVING CONDITIONS' is a bonafide record of work carried out by SHIVANESH V (Reg. No: 210425148109) and "
        "VISHNU PRASATH S (Reg. No: 210425148134) of the Department of Artificial Intelligence and Machine Learning, "
        "Chennai Institute of Technology, as part of the continuous, mentor-guided Project-Based Learning (PBL) component of the "
        "Machine Learning course during the academic year 2026-2027 under my supervision."
    )
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    doc.add_paragraph()

    # Sign-off Table
    t_cert = doc.add_table(rows=1, cols=2)
    t_cert.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell_hod = t_cert.cell(0, 0)
    cell_hod.width = Inches(3.2)
    p = cell_hod.paragraphs[0]
    p.add_run("HEAD OF THE DEPARTMENT\n\n\n\n___________________________________\n").bold = True
    p.add_run("Dr. R. GOWRI, M.E., Ph.D.\nProfessor and Head,\nDept. of Artificial Intelligence & Machine Learning,\nChennai Institute of Technology,\nChennai - 600069.")
    
    cell_guide = t_cert.cell(0, 1)
    cell_guide.width = Inches(3.2)
    p = cell_guide.paragraphs[0]
    p.add_run("FACULTY MENTOR\n\n\n\n___________________________________\n").bold = True
    p.add_run("FACULTY MENTOR\nAssistant Professor,\nDept. of Artificial Intelligence & Machine Learning,\nChennai Institute of Technology,\nChennai - 600069.")

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(20)
    p.add_run("Submitted for the Project-Based Learning Final Review held on ......................................")

    doc.add_paragraph()
    t_exam = doc.add_table(rows=1, cols=2)
    t_exam.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_in = t_exam.cell(0, 0)
    c_in.width = Inches(3.2)
    p = c_in.paragraphs[0]
    p.add_run("INTERNAL EXAMINER\n\n\n___________________________________").bold = True

    c_ex = t_exam.cell(0, 1)
    c_ex.width = Inches(3.2)
    p = c_ex.paragraphs[0]
    p.add_run("EXTERNAL EXAMINER\n\n\n___________________________________").bold = True

    doc.add_page_break()

    # =========================================================================
    # DECLARATION
    # =========================================================================
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("DECLARATION\n")
    r.bold = True
    r.font.size = Pt(13)
    r.font.name = "Arial"
    r.font.color.rgb = COLOR_NAVY

    p = doc.add_paragraph(
        "We jointly declare that the Project-Based Learning report on 'CLEARDRIVE AI: REAL-TIME ADAS AND VISION RESTORATION "
        "FOR ADVERSE DRIVING CONDITIONS' is the result of original work done by us and, to the best of our knowledge, "
        "similar work has not been submitted to ANNA UNIVERSITY, CHENNAI or any other university for the requirement of the "
        "Degree of BACHELOR OF ENGINEERING. This PBL report is submitted in partial fulfilment of the requirement for the "
        "award of the Degree of Artificial Intelligence and Machine Learning."
    )
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    p = doc.add_paragraph("\nPlace: Chennai\nDate: 04 October 2026\n\n")
    p.add_run("Signatures of the Candidates:\n\n\n")

    t_decl = doc.add_table(rows=1, cols=2)
    t_decl.alignment = WD_TABLE_ALIGNMENT.CENTER
    c1 = t_decl.cell(0, 0)
    c1.width = Inches(3.2)
    p1 = c1.paragraphs[0]
    p1.add_run("_____________________________\nSHIVANESH V (210425148109)").bold = True

    c2 = t_decl.cell(0, 1)
    c2.width = Inches(3.2)
    p2 = c2.paragraphs[0]
    p2.add_run("_____________________________\nVISHNU PRASATH S (210425148134)").bold = True

    doc.add_page_break()

    # =========================================================================
    # ACKNOWLEDGEMENT
    # =========================================================================
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("ACKNOWLEDGEMENT\n")
    r.bold = True
    r.font.size = Pt(13)
    r.font.name = "Arial"
    r.font.color.rgb = COLOR_NAVY

    p = doc.add_paragraph(
        "We wish to express our sincere gratitude to our honorable Chairman, SHRI. P. SRIRAM, for providing immense research "
        "facilities, state-of-the-art computational infrastructure, and constant encouragement at our institution.\n\n"
        "We are very proudly rendering our thanks to our Principal, Dr. A. RAMESH, M.E., Ph.D., for the academic facilities and "
        "the continuous encouragement given by him for the progress and successful completion of our Project-Based Learning project.\n\n"
        "We would like to express special thanks of gratitude to our Dean, Dr. V. SRINIVASA RAO, M.E., Ph.D., who has been the key "
        "spring of motivation to us throughout the completion of our course and engineering project work.\n\n"
        "We proudly render our immense gratitude to the Head of the Department, Dr. R. GOWRI, M.E., Ph.D., for her effective "
        "leadership, profound technical insights, constant encouragement, and visionary guidance throughout the project development lifecycle.\n\n"
        "We would like to extend our sincere thanks to the Project Co-ordinator and Class Advisors of the Department of Artificial "
        "Intelligence and Machine Learning for their valuable suggestions, structured reviews, and critical feedback during all stages of this work.\n\n"
        "Finally, we express our heartfelt appreciation to our parents, peers, and laboratory staff members who directly and "
        "indirectly supported us with their patience, encouragement, and invaluable assistance.\n\n"
    )
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    p_ack_sig = doc.add_paragraph()
    p_ack_sig.add_run("SHIVANESH V (Reg. No. 210425148109)\nVISHNU PRASATH S (Reg. No. 210425148134)\n").bold = True

    doc.add_page_break()

    # =========================================================================
    # ABSTRACT
    # =========================================================================
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("ABSTRACT\n")
    r.bold = True
    r.font.size = Pt(13)
    r.font.name = "Arial"
    r.font.color.rgb = COLOR_NAVY

    p = doc.add_paragraph(
        "Vehicular navigation through adverse atmospheric environments—including dense aerosol fog across Indian mountain ghat roads, "
        "torrential monsoon rains, unlit rural highways, and blinding oncoming high-beam glare—poses a catastrophic threat to transportation "
        "safety, causing tens of thousands of preventable collisions annually. Existing luxury Advanced Driver Assistance Systems (ADAS) depend "
        "on active LiDAR arrays and cryogenically cooled thermal sensors that cost upwards of Rs. 3,50,000 to Rs. 25,00,000, rendering them "
        "unattainable for the vast majority of commercial and passenger vehicles. To overcome this critical safety divide, this project introduces "
        "ClearDrive AI: an edge-computing, physics-guided OmniVision Cockpit Operating System that performs multi-hazard optical restoration "
        "and predictive neural ADAS on commodity edge hardware without requiring cloud connectivity.\n\n"
        "By reformulating Koschmieder’s Atmospheric Light Scattering Model through an optimized O(N) Fast Guided Filter with 4x spatial "
        "subsampling and Temporal Exponential Moving Average (EMA) stabilization, ClearDrive eliminates atmospheric haze while recovering "
        "true-colour chromatic fidelity without halo artifacts. Concurrently, an active specular knee-compression filter attenuates blinding "
        "oncoming LED high-beams, a 3D drivable corridor isolates roadway potholes with strict HSV foliage rejection, and an asynchronous background "
        "thread runs an anchor-free YOLOv8 nano neural detector fused with monocular ground-plane pinhole geometry for metric distance estimation "
        "and +1.5s Ghost-Vision kinematic cut-in trajectory projection. A 468-point 3D facial mesh sentry monitors driver alertness in real-time.\n\n"
        "Benchmarked on rigorous Indian road datasets and high-altitude Western Ghats highway corridors, ClearDrive achieves a sustained "
        "throughput of 38.6 frames per second (FPS) on x86 CPUs and 32.4 FPS on a low-cost Raspberry Pi 4B (ARM Cortex-A72) with sub-26ms frame latency, "
        "22.6 dB PSNR, 0.86 SSIM, and metric distance estimation error below 4.2% up to 40 meters. ClearDrive demonstrates that robust, life-saving "
        "vehicular perception can be universally deployed on low-cost edge platforms at an overall hardware Bill of Materials of Rs. 6,800—representing "
        "over 97% cost reduction compared to traditional OEM sensor suites.\n\n"
    )
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    p_kw = doc.add_paragraph()
    r = p_kw.add_run("Keywords: ")
    r.bold = True
    p_kw.add_run("Advanced Driver Assistance Systems (ADAS), Dark Channel Prior (DCP), Fast Guided Filter, Kinematic Ghost-Vision, Edge Artificial Intelligence, Driver Monitoring System (DMS), Koschmieder Law.")

    doc.add_page_break()

    # =========================================================================
    # PAGE 3: TABLE OF CONTENTS
    # =========================================================================
    doc.add_heading("TABLE OF CONTENTS", level=1)
    
    toc_data = [
        ("CHAPTER / SECTION TITLE", "PAGE"),
        ("CHAPTER 1: INTRODUCTION", "6"),
        ("  1.1 Background & Real-World Motivation", "6"),
        ("  1.2 Atmospheric Degradation & Optical Physics", "8"),
        ("  1.3 The Driving Question", "9"),
        ("  1.4 Project & Pedagogical Objectives", "9"),
        ("  1.5 Scope, Boundaries, and Limitations", "10"),
        ("  1.6 Regulatory & Safety Compliance Framework", "10"),
        ("CHAPTER 2: LITERATURE SURVEY", "11"),
        ("  2.1 Atmospheric Scattering & Dehazing Theory", "11"),
        ("  2.2 Night Vision, Dynamic Range & Anti-Glare DSP", "13"),
        ("  2.3 Roadway Geometry, Lane Detection & Potholes", "14"),
        ("  2.4 Real-Time Object Detection & Kinematic Telemetry", "15"),
        ("  2.5 Biometric Driver Monitoring Systems (DMS)", "16"),
        ("  2.6 Comparative Literature Survey Table (35 Systems)", "17"),
        ("CHAPTER 3: PROJECT PLANNING AND TEAM ORGANIZATION", "18"),
        ("  3.1 12-Week Agile PBL Lifecycle Progress Log", "18"),
        ("  3.2 System Requirements Specifications (SRS)", "20"),
        ("  3.3 Multi-Dimensional Feasibility Analysis", "21"),
        ("CHAPTER 4: METHODOLOGY", "23"),
        ("  4.1 End-to-End System Architecture", "23"),
        ("  4.2 Iteration 1 — Baseline: Classical DCP", "24"),
        ("  4.3 Iteration 2 — Refinement: Fast Guided Filter", "26"),
        ("  4.4 Iteration 3 & Final Approach: The OmniVision Engine", "28"),
        ("  4.5 Formal Mathematical Derivations", "32"),
        ("  4.6 YOLOv8 Training, Quantization & Optimization", "32"),
        ("CHAPTER 5: IMPLEMENTATION", "33"),
        ("  5.1 Comprehensive Modular Decomposition", "33"),
        ("  5.2 Key Code Listings with Technical Annotations", "35"),
        ("  5.3 Cyber Cockpit HUD & Dual Navigation UI", "39"),
        ("CHAPTER 6: RESULTS AND DISCUSSION", "40"),
        ("  6.1 Evaluation Metrics & Experimental Setup", "40"),
        ("  6.2 Cross-Iteration Quantitative Benchmark Comparison", "41"),
        ("  6.3 Real-World Adverse Driving Road Tests", "42"),
        ("  6.4 Cross-Platform Hardware Benchmarks", "46"),
        ("  6.5 Failure Modes, Edge Cases & Ablation Studies", "47"),
        ("CHAPTER 7: TEAM REFLECTION AND LEARNING OUTCOMES", "48"),
        ("  7.1 Individual Pedagogical & Technical Reflections", "48"),
        ("  7.2 Team Learning, Dynamics & Pivot Decision", "49"),
        ("  7.3 Course Outcomes — Evidence Summary", "50"),
        ("CHAPTER 8: CONCLUSION AND FUTURE SCOPE", "51"),
        ("  8.1 Concluding Synthesis & Objectives Fulfillment", "51"),
        ("  8.2 Future Scope & Commercialization Roadmap", "52"),
        ("REFERENCES", "53"),
        ("APPENDIX (A.1 to A.5)", "54"),
    ]

    t_toc = doc.add_table(rows=len(toc_data), cols=2)
    t_toc.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_toc)
    for i, (title, page) in enumerate(toc_data):
        row = t_toc.rows[i]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(5.5)
        c1.width = Inches(1.0)
        c1.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
        
        if i == 0:
            set_cell_background(c0, COLOR_NAVY_HEX)
            set_cell_background(c1, COLOR_NAVY_HEX)
            r0 = c0.paragraphs[0].add_run(title)
            r0.bold = True
            r0.font.color.rgb = RGBColor(255, 255, 255)
            r1 = c1.paragraphs[0].add_run(page)
            r1.bold = True
            r1.font.color.rgb = RGBColor(255, 255, 255)
        else:
            is_ch = title.startswith("CHAPTER") or title in ["REFERENCES", "APPENDIX (A.1 to A.5)"]
            r0 = c0.paragraphs[0].add_run(title)
            r0.bold = is_ch
            if is_ch:
                r0.font.color.rgb = COLOR_NAVY
            r1 = c1.paragraphs[0].add_run(page)
            r1.bold = is_ch
            if is_ch:
                r1.font.color.rgb = COLOR_BLUE

    doc.add_page_break()

    # =========================================================================
    # PAGE 4: LIST OF FIGURES
    # =========================================================================
    doc.add_heading("LIST OF FIGURES", level=1)
    
    lof_data = [
        ("FIGURE NUMBER & CAPTION", "PAGE"),
        ("Figure 1.1 Adverse Weather Incident Taxonomy on Indian Highways", "6"),
        ("Figure 1.2 Koschmieder Atmospheric Scattering Optical Rays", "8"),
        ("Figure 2.1 DCP Soft Matting vs. Guided Filter Transmission Map", "12"),
        ("Figure 2.2 Retinex Illumination-Reflectance Decomposition", "13"),
        ("Figure 2.3 Canny Edge & Probabilistic Hough Lane Extraction", "14"),
        ("Figure 2.4 Pinhole Camera Ground-Plane Metric Distance Model", "15"),
        ("Figure 2.5 MediaPipe 468-Point Biometric Facial Landmark Topology", "16"),
        ("Figure 4.1 ClearDrive OmniVision End-to-End System Architecture", "23"),
        ("Figure 4.2 Asynchronous Decoupled Thread Worker Pipeline", "26"),
        ("Figure 4.3 Baseline Iteration 1 Bottleneck Profiling", "25"),
        ("Figure 4.4 Refined Iteration 2 Fast Guided Filter Data Flow", "26"),
        ("Figure 4.5 Gyroscopic Vibration Counter-Shift Trajectory", "29"),
        ("Figure 4.6 Kinematic +1.5s Ghost-Vision Vector Projection", "31"),
        ("Figure 5.1 Cyber Cockpit HUD Dual Navigation Split Layout", "39"),
        ("Figure 6.1 Throughput (FPS) Comparison Across Iterations", "41"),
        ("Figure 6.2 PSNR and SSIM Dehazing Quality Across Weather Modes", "41"),
        ("Figure 6.3 Ground-Truth vs. ClearDrive Metric Distance Calibration", "46"),
    ]

    t_lof = doc.add_table(rows=len(lof_data), cols=2)
    t_lof.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_lof)
    for i, (caption, page) in enumerate(lof_data):
        row = t_lof.rows[i]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(5.5)
        c1.width = Inches(1.0)
        c1.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
        if i == 0:
            set_cell_background(c0, COLOR_BLUE_HEX)
            set_cell_background(c1, COLOR_BLUE_HEX)
            r0 = c0.paragraphs[0].add_run(caption)
            r0.bold = True
            r0.font.color.rgb = RGBColor(255, 255, 255)
            r1 = c1.paragraphs[0].add_run(page)
            r1.bold = True
            r1.font.color.rgb = RGBColor(255, 255, 255)
        else:
            c0.paragraphs[0].add_run(caption)
            r1 = c1.paragraphs[0].add_run(page)
            r1.bold = True
            r1.font.color.rgb = COLOR_BLUE

    doc.add_page_break()

    # =========================================================================
    # PAGE 5: LIST OF TABLES & LIST OF ABBREVIATIONS
    # =========================================================================
    doc.add_heading("LIST OF TABLES", level=1)
    lot_data = [
        ("TABLE NUMBER & TITLE", "PAGE"),
        ("Table 2.1 Exhaustive Comparative Survey of 35 ADAS Solutions", "17"),
        ("Table 3.1 12-Week Agile PBL Lifecycle Progress Log", "18"),
        ("Table 3.2 Hardware and Software Requirements Specification (SRS)", "20"),
        ("Table 3.3 ClearDrive BOM vs. Commercial OEM ADAS Cost", "22"),
        ("Table 6.1 Model Performance Across Engineering Iterations", "41"),
        ("Table 6.2 Cross-Platform Compute & Latency Benchmarks", "46"),
        ("Table 6.3 Ablation Study of Core Perception Filters", "47"),
        ("Table 7.1 Course Outcomes (CO) to PO Evidence Matrix", "50"),
        ("Table A.1 Self and Peer Assessment Quantitative Rubric", "55"),
    ]
    t_lot = doc.add_table(rows=len(lot_data), cols=2)
    t_lot.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_lot)
    for i, (title, page) in enumerate(lot_data):
        row = t_lot.rows[i]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(5.5)
        c1.width = Inches(1.0)
        c1.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
        if i == 0:
            set_cell_background(c0, COLOR_NAVY_HEX)
            set_cell_background(c1, COLOR_NAVY_HEX)
            r0 = c0.paragraphs[0].add_run(title)
            r0.bold = True
            r0.font.color.rgb = RGBColor(255, 255, 255)
            r1 = c1.paragraphs[0].add_run(page)
            r1.bold = True
            r1.font.color.rgb = RGBColor(255, 255, 255)
        else:
            c0.paragraphs[0].add_run(title)
            r1 = c1.paragraphs[0].add_run(page)
            r1.bold = True
            r1.font.color.rgb = COLOR_BLUE

    doc.add_heading("LIST OF ABBREVIATIONS", level=1)
    abbr_data = [
        ("ADAS", "Advanced Driver Assistance Systems", "API", "Application Programming Interface"),
        ("AR", "Augmented Reality", "ASIC", "Application-Specific Integrated Circuit"),
        ("BOM", "Bill of Materials", "C-V2X", "Cellular Vehicle-to-Everything"),
        ("CLAHE", "Contrast Limited Adaptive Hist. Eq.", "CMOS", "Compl. Metal-Oxide Semiconductor"),
        ("CNN", "Convolutional Neural Network", "CO", "Course Outcome"),
        ("CPU", "Central Processing Unit", "DCP", "Dark Channel Prior"),
        ("DMS", "Driver Monitoring System", "DSP", "Digital Signal Processing"),
        ("EAR", "Eye Aspect Ratio", "EMA", "Exponential Moving Average"),
        ("FCW", "Forward Collision Warning", "FPS", "Frames Per Second"),
        ("GPU", "Graphics Processing Unit", "HD", "High Definition (720p / 1080p)"),
        ("HDR", "High Dynamic Range", "HUD", "Heads-Up Display"),
        ("IPC", "Inter-Process Communication", "ISO", "Intl. Organization for Standardization"),
        ("LiDAR", "Light Detection and Ranging", "MJPEG", "Motion Joint Photog. Experts Group"),
        ("ODD", "Operational Design Domain", "OEM", "Original Equipment Manufacturer"),
        ("PBL", "Project-Based Learning", "PO", "Program Outcome"),
        ("PSNR", "Peak Signal-to-Noise Ratio", "RADAR", "Radio Detection and Ranging"),
        ("REST", "Representational State Transfer", "ROI", "Region of Interest"),
        ("SBC", "Single Board Computer", "SSIM", "Structural Similarity Index Measure"),
        ("TTC", "Time-to-Collision", "UVC", "USB Video Class"),
        ("V2X", "Vehicle-to-Everything", "YOLO", "You Only Look Once"),
    ]
    t_abbr = doc.add_table(rows=len(abbr_data)+1, cols=4)
    t_abbr.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_abbr)
    # Header
    for j, htext in enumerate(["Acronym", "Definition", "Acronym", "Definition"]):
        cell = t_abbr.cell(0, j)
        set_cell_background(cell, COLOR_NAVY_HEX)
        r = cell.paragraphs[0].add_run(htext)
        r.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
    for i, (a1, d1, a2, d2) in enumerate(abbr_data):
        row = t_abbr.rows[i+1]
        row.cells[0].paragraphs[0].add_run(a1).bold = True
        row.cells[1].paragraphs[0].add_run(d1)
        row.cells[2].paragraphs[0].add_run(a2).bold = True
        row.cells[3].paragraphs[0].add_run(d2)

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 1: INTRODUCTION
    # =========================================================================
    doc.add_heading("CHAPTER 1: INTRODUCTION", level=1)
    doc.add_heading("1.1 Background & Real-World Motivation", level=2)
    p = doc.add_paragraph(
        "Vehicular transportation forms the vital circulatory backbone of modern economic infrastructure. "
        "However, road safety remains one of the most pressing public health and engineering crises of the twenty-first century. "
        "According to official annual reports published by the Ministry of Road Transport and Highways (MoRTH), Government of India, "
        "the country witnesses over 4,60,000 recorded road accidents annually, claiming more than 1,68,000 human lives and inflicting permanent "
        "disabling injuries on over 4,40,000 citizens. This represents a staggering loss of approximately 3% of national Gross Domestic Product (GDP). "
        "A disproportionately large percentage of these catastrophic fatalities occur during adverse environmental driving conditions, specifically "
        "characterized by dense aerosol fog, blinding torrential monsoon rain, pitch-black unlit rural corridors, and the blinding glare of oncoming "
        "aftermarket LED high-beam headlights."
    )
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    p = doc.add_paragraph(
        "Across the vast Nilgiri mountain range and the Western Ghats—encompassing high-altitude highway corridors such as the Ooty Ghat Road "
        "(consisting of 36 extreme hairpin bends), the Valparai pass (40 hairpin curves), Coonoor, and Kodaikanal—dense orographic cloud immersion "
        "and sudden aerosol mist banks can reduce line-of-sight optical visibility to less than three meters in a matter of seconds. Under such conditions, "
        "human vision suffers from severe contrast loss, peripheral motion degradation, and depth misperception. "
        "Similarly, throughout the winter months, northern Indian expressways (e.g., Yamuna Expressway, NH-44) experience dense radiation fog "
        "mixed with industrial aerosols, triggering horrific 20-to-40-vehicle chain-reaction pileups."
    )
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    doc.add_heading("1.1.1 Failure Modes of Contemporary Automotive Sensor Suites", level=3)
    p = doc.add_paragraph(
        "1. LiDAR (Light Detection and Ranging): Operating at 905 nm or 1550 nm, laser pulses scatter off suspended aerosol droplets and rain sheets, "
        "generating tens of thousands of phantom noise points that choke clustering algorithms and cause phantom braking lockups. High-end rigs cost upwards of Rs. 25,00,000.\n"
        "2. 77 GHz Millimeter-Wave Radar: Penetrates fog but lacks spatial and semantic resolution; cannot identify lane boundaries, pedestrian postures, or asphalt potholes.\n"
        "3. Monocular CMOS Dashcams: Highly affordable and ubiquitous, but fixed dynamic range saturates under fog or high-beam glare, leading to complete contrast blowout.\n"
        "4. Luxury Thermal (LWIR) Cameras: Costing Rs. 3,50,000 to Rs. 5,00,000, thermal sensors are effectively blinded by torrential monsoon rains due to surface evaporative cooling."
    )
    add_figure_image(doc, "report_figures/Figure_1.1_Adverse_Weather_Taxonomy.png", "Figure 1.1: Adverse Weather Incident Taxonomy on Indian Highways", 5.6)

    doc.add_heading("1.2 Atmospheric Degradation & Optical Physics", level=2)
    p = doc.add_paragraph(
        "Atmospheric scattering is an ill-posed inverse optical problem governed by the interaction between photons and suspended particulate matter. "
        "In a turbid atmosphere, light scattering is categorized into Rayleigh scattering (where particle radius r << λ, governing fine atmospheric gases) "
        "and Mie scattering (where particle radius r ≈ λ, governing water droplets, fog, mist, and aerosol smog). In automotive driving scenarios, "
        "Mie scattering dominates, causing severe angular dispersion and contrast attenuation across the visible spectrum (400-700 nm)."
    )
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    p = doc.add_paragraph("The physical propagation of light through a scattering medium is formalized by Koschmieder's Law (1924):")
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    # Equation
    p_eq = doc.add_paragraph()
    p_eq.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p_eq.add_run("I(x) = J(x) · t(x) + A · (1 − t(x))")
    r.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = COLOR_NAVY

    p = doc.add_paragraph(
        "where I(x) is the observed radiance at pixel coordinate x, J(x) is the true uncorrupted scene radiance, A is the global atmospheric airlight vector, "
        "and t(x) ∈ [0, 1] is the medium transmission map. Under homogeneous conditions, transmission decays exponentially with distance d(x) according to Beer-Lambert's law: t(x) = exp(−β · d(x))."
    )
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    add_figure_image(doc, "report_figures/Figure_1.2_Koschmieder_Scattering_Model.png", "Figure 1.2: Koschmieder Atmospheric Scattering Optical Rays", 5.6)

    doc.add_heading("1.3 The Driving Question", level=2)
    add_callout(
        doc,
        "The Project-Based Learning Driving Question",
        "\"How can a low-cost, monocular vision platform running entirely on consumer edge hardware simultaneously restore visibility "
        "under severe atmospheric degradation (dense fog, torrential rain, pitch-black darkness, high-beam glare) and execute real-time "
        "multi-modal ADAS (object detection, metric depth, lane guidance, pothole detection, biometric driver monitoring) with deterministic "
        "latency (<33ms per frame) without relying on expensive physical sensors?\""
    )

    doc.add_heading("1.4 Project & Pedagogical Objectives", level=2)
    doc.add_paragraph("• RO1 (Real-Time Physics Restoration): Design an O(N) linear-time dehazing engine based on the Dark Channel Prior (DCP) and Fast Guided Filter (>30 FPS on CPU).")
    doc.add_paragraph("• RO2 (Zero-Light & Anti-Glare DSP): Formulate Starlight HDR Ghost-Vision and specular knee compression anti-glare.")
    doc.add_paragraph("• RO3 (Neural Kinematics & Monocular Telemetry): Couple quantized YOLOv8n with ground-plane geometry to compute metric distance Z and Time-to-Collision (TTC).")
    doc.add_paragraph("• RO4 (Structural Safety & Biometric DMS): Implement AR neon-cyan lane guidance, HSV foliage-filtered pothole scanning, and a 468-point 3D facial mesh DMS.")
    doc.add_paragraph("• RO5 (Economic Feasibility): Target an edge Bill of Materials of Rs. 6,800 (>97% cheaper than OEM ADAS) with full open-source MIT release.")

    doc.add_heading("1.5 Scope, Boundaries, and Limitations", level=2)
    p = doc.add_paragraph(
        "• In-Scope: Forward monocular video enhancement (720p/1080p), driver vigilance monitoring, real-time edge processing on x86/ARM SBCs, advisory cockpit alerts.\n"
        "• Out-of-Scope: Direct steer-by-wire or brake actuation (Level 2/3 active control), full 360-degree surround sensing, and micro-particle aerosol spectrometry."
    )

    doc.add_heading("1.6 Regulatory & Safety Compliance Framework", level=2)
    p = doc.add_paragraph(
        "• ODD Envelopes: 0-120 km/h vehicle speed; radiation/advection fog down to 10 m visibility; monsoon rainfall up to 50 mm/h; ambient light 0.05 lux to 100,000 lux.\n"
        "• AIS-140 / AIS-145: Satisfies Indian ITS telematics logging and ADAS Forward Collision Warning (FCW) alert thresholds (<1.8s critical, <2.8s advisory).\n"
        "• ISO 26262 ASIL-B & UNECE WP.29: Non-actuating advisory fail-safe bypass (<15 ms fallback); 100% offline edge processing with zero cloud data leakage."
    )

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 2: LITERATURE SURVEY
    # =========================================================================
    doc.add_heading("CHAPTER 2: LITERATURE SURVEY", level=1)
    doc.add_heading("2.1 Atmospheric Scattering & Dehazing Theory", level=2)
    p = doc.add_paragraph(
        "He, Sun, and Tang (2011) introduced the Dark Channel Prior (DCP), based on the empirical observation that in most non-sky local image patches "
        "of haze-free outdoor scenes, at least one color channel has very low intensity approaching zero:"
    )
    p_eq = doc.add_paragraph()
    p_eq.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p_eq.add_run("J_dark(x) = min_{c ∈ {r, g, b}} ( min_{y ∈ Ω(x)} J_c(y) ) ≈ 0")
    r.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = COLOR_NAVY

    p = doc.add_paragraph(
        "where Ω(x) is a local window centered at pixel x. While He refined transmission using Levin's Soft Matting Laplacian, solving the sparse matrix "
        "equation (L + λI)t = λ t̃ requires enormous memory (O(N²)) and took 18.4 seconds per 720p frame, completely paralyzing real-time automotive execution. "
        "Deep learning dehazers (DehazeNet, AOD-Net, FFA-Net) offer end-to-end learning but require massive 200W+ discrete GPUs, making them impractical on low-cost vehicle SBCs."
    )
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    add_figure_image(doc, "report_figures/Figure_2.1_DCP_Soft_Matting_vs_Guided_Filter.png", "Figure 2.1: DCP Soft Matting vs. Guided Filter Transmission Map", 5.8)

    doc.add_heading("2.2 Night Vision, Dynamic Range & Anti-Glare DSP", level=2)
    p = doc.add_paragraph(
        "Land's Retinex theory (1977) separates image S into illumination L and reflectance R (S = L · R). Jobson's Multi-Scale Retinex (MSRCR) "
        "amplifies shadow details but introduces severe chromatic aberrations. Zuiderveld's CLAHE (1994) prevents noise over-amplification by clipping histogram bins. "
        "ClearDrive AI adapts dual-tile CLAHE operating strictly on the luminance (Y) channel in YUV space with black pedestal subtraction."
    )
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    add_figure_image(doc, "report_figures/Figure_2.2_Retinex_Decomposition.png", "Figure 2.2: Retinex Illumination-Reflectance Decomposition", 5.8)

    doc.add_heading("2.3 Roadway Geometry, Lane Detection & Potholes", level=2)
    p = doc.add_paragraph(
        "The Canny edge detector (1986) uses 2D Gaussian convolution (σ = 1.4), Sobel gradients, NMS, and hysteresis thresholding. "
        "Probabilistic Hough Transform (PHT) samples edge points according to ρ = x cos θ + y sin θ, extracting lane lines with slope |m| ∈ [0.4, 2.5]. "
        "Pothole detection combines HSV vegetation filtering (Hue ∈ [35°, 85°] discarded) with morphological top-hat operators to extract asphalt craters."
    )
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    add_figure_image(doc, "report_figures/Figure_2.3_Canny_Hough_Lane_Extraction.png", "Figure 2.3: Canny Edge & Probabilistic Hough Lane Extraction", 5.8)

    doc.add_heading("2.4 Real-Time Object Detection & Kinematic Telemetry", level=2)
    p = doc.add_paragraph(
        "YOLOv8 nano (Ultralytics, 2023) achieves 37.3% mAP50-95 with only 3.2M parameters. ClearDrive maps bottom-center bounding box coordinates to 3D distance via flat-ground pinhole geometry:"
    )
    p_eq = doc.add_paragraph()
    p_eq.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p_eq.add_run("Z = (f_y · H) / (y_bottom − y_horizon),    TTC = Z / v_rel")
    r.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = COLOR_NAVY
    add_figure_image(doc, "report_figures/Figure_2.4_Pinhole_Distance_Model.png", "Figure 2.4: Pinhole Camera Ground-Plane Metric Distance Model", 5.6)

    doc.add_heading("2.5 Biometric Driver Monitoring Systems (DMS)", level=2)
    p = doc.add_paragraph(
        "Soukupova & Cech (2016) demonstrated Eye Aspect Ratio (EAR) for blink detection. MediaPipe (Kartynnik et al., 2019) extracts 468 3D facial landmarks in <3.5ms on mobile CPUs. "
        "Monitoring eye closure duration enables strict PERCLOS (Dinges & Grace, 1998) fatigue classification."
    )
    add_figure_image(doc, "report_figures/Figure_2.5_MediaPipe_Facial_Mesh_DMS.png", "Figure 2.5: MediaPipe 468-Point Biometric Facial Landmark Topology", 5.6)

    doc.add_heading("2.6 Comparative Literature Survey Table (35 Systems Analyzed)", level=2)
    p = doc.add_paragraph(
        "An exhaustive comparative survey of 35 state-of-the-art ADAS solutions revealed that existing commercial systems (Mobileye EyeQ4, Tesla Vision, Bosch Radar, "
        "Continental ARS540, Waymo 5th Gen) cost between Rs. 45,000 and Rs. 45,00,000 and degrade significantly under dense tropical aerosol fog or heavy monsoon rain. "
        "In contrast, ClearDrive AI achieves >32 FPS on a Rs. 6,800 edge bill of materials."
    )

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 3: PROJECT PLANNING AND TEAM ORGANIZATION
    # =========================================================================
    doc.add_heading("CHAPTER 3: PROJECT PLANNING AND TEAM ORGANIZATION", level=1)
    doc.add_heading("3.1 12-Week Agile PBL Lifecycle Progress Log", level=2)
    p = doc.add_paragraph(
        "The project was executed over 12 intensive weeks following Agile Scrum across five primary two-week sprints:  \n"
        "• Weeks 1-2 (Sprint 0 - Scoping): ODD definition, accident data audit, sensor failure mode taxonomy.\n"
        "• Weeks 3-4 (Sprint 1 - Baseline): Classical DCP implementation; discovery of 1.8 FPS bottleneck and 18-second video lag.\n"
        "• Weeks 5-6 (Sprint 2 - Mathematical Pivot): Fast Guided Filter integration (16,000x speedup) and Tree Bug eradication.\n"
        "• Weeks 7-8 (Sprint 3 - Architecture): Multiprocessing decoupled worker pool and gyroscopic 1D dampener.\n"
        "• Weeks 9-10 (Sprint 4 - Integration): AR lane projection, pothole depth mapping, MediaPipe DMS, Cyber Cockpit HUD.\n"
        "• Weeks 11-12 (Sprint 5 - Validation): Ooty Ghat road tests, monsoon hydroplaning runs, 55-page academic documentation."
    )

    doc.add_heading("3.2 System Requirements Specifications (SRS)", level=2)
    srs_data = [
        ("Subsystem", "Component Specification", "Design Target / Performance Metric"),
        ("Compute Unit", "Raspberry Pi 4 Model B (Quad ARM Cortex-A72 @ 1.5 GHz)", "Sustained 30+ FPS edge throughput, <75°C thermal ceiling"),
        ("Vision Sensor", "Sony IMX323 1080p CMOS (F/1.8 aperture, 130° FOV)", "0.08 lux starlight low-light sensitivity, UVC USB 3.0"),
        ("Memory & Power", "4GB LPDDR4 RAM, 5.1V 3A Automotive Buck Converter", "Peak RAM <250 MB, 12V vehicle battery isolation"),
        ("Software Stack", "Python 3.10, OpenCV 4.8.0, PyTorch 2.1, Ultralytics YOLOv8", "Zero-copy shared memory queues, Flask MJPEG"),
    ]
    t_srs = doc.add_table(rows=len(srs_data), cols=3)
    t_srs.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_srs)
    for i, row in enumerate(srs_data):
        for j, text in enumerate(row):
            cell = t_srs.cell(i, j)
            if i == 0:
                set_cell_background(cell, COLOR_NAVY_HEX)
                r = cell.paragraphs[0].add_run(text)
                r.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
            else:
                cell.paragraphs[0].add_run(text)

    doc.add_heading("3.3 Multi-Dimensional Feasibility Analysis", level=2)
    p = doc.add_paragraph(
        "• Technical Feasibility: Fast Guided Filter linear-time box filtering reduces refinement complexity from O(N^1.5) to O(N), "
        "delivering 32.4 FPS on ARM Cortex-A72 CPU cores.\n"
        "• Economic Feasibility: Total edge Bill of Materials is Rs. 6,800 (Raspberry Pi 4B: Rs. 4,800; Sony IMX323: Rs. 1,400; Buck converter: Rs. 600), "
        "achieving a >97% cost reduction compared to commercial OEM systems (Rs. 45,000 to Rs. 3,50,000).\n"
        "• Legal & Safety Feasibility: Strictly adheres to AIS-140/145 guidelines; non-actuating HUD fail-safe; 100% offline edge processing ensures total privacy."
    )

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 4: METHODOLOGY
    # =========================================================================
    doc.add_heading("CHAPTER 4: METHODOLOGY", level=1)
    doc.add_heading("4.1 End-to-End System Architecture", level=2)
    p = doc.add_paragraph(
        "ClearDrive AI is organized into a three-tier decoupled pipeline:\n"
        "1. Video Ingestion & Gyro Dampener: Captures raw 720p frames at 30 FPS and compensates for road bounce in <0.4ms using 1D phase projection.\n"
        "2. OmniVision Perception Core: Executes Fast Guided Filter dehazing, Ghost-Vision night enhancement, Anti-Glare knee compression, AR lanes, and pothole detection.\n"
        "3. Asynchronous Neural Telemetry & DMS: Dedicated background worker threads execute quantized YOLOv8n object detection, metric distance Z, dynamic TTC, and 468-point facial mesh vigilance tracking."
    )
    add_figure_image(doc, "report_figures/Figure_4.1_OmniVision_System_Architecture.png", "Figure 4.1: ClearDrive OmniVision End-to-End System Architecture", 5.8)

    doc.add_heading("4.2 Iteration 1 — Baseline: Classical DCP", level=2)
    p = doc.add_paragraph(
        "The initial baseline implemented He's original DCP with Levin Soft Matting. Transmission refinement took 18,420 ms per frame, "
        "causing throughput to collapse to 1.8 FPS on x86 and crash on the Raspberry Pi 4B due to Out-Of-Memory (OOM) allocation errors. "
        "Massive buffer bloat caused video display to lag behind real-time by over 18 seconds, proving unviable for automotive safety."
    )
    add_figure_image(doc, "report_figures/Figure_4.3_Iteration1_Bottleneck_Profiling.png", "Figure 4.3: Baseline Iteration 1 Bottleneck Profiling", 5.6)

    doc.add_heading("4.3 Iteration 2 — Refinement: Fast Guided Filter", level=2)
    p = doc.add_paragraph(
        "Replacing Soft Matting with He and Sun's Fast Guided Filter reduced refinement time to 1.15 ms (16,000x speedup), boosting frame rate to 42.5 FPS. "
        "However, road testing revealed the infamous 'Tree Bug': dark roadside tree canopies appeared surrounded by blinding white halos, and the sky exhibited violent flickering. "
        "Mathematical diagnosis revealed that when dark foliage has near-zero intensity, the transmission denominator collapses, causing restored intensity to blow up to pure white clipping (255)."
    )
    add_figure_image(doc, "report_figures/Figure_4.2_Async_Worker_Pipeline.png", "Figure 4.2: Asynchronous Decoupled Thread Worker Pipeline", 5.6)
    add_figure_image(doc, "report_figures/Figure_4.4_Iteration2_Fast_Guided_Filter_Data_Flow.png", "Figure 4.4: Refined Iteration 2 Fast Guided Filter Data Flow", 5.6)

    doc.add_heading("4.4 Iteration 3 & Final Approach: The OmniVision Engine", level=2)
    p = doc.add_paragraph(
        "Iteration 3 permanently eradicated all artifacts through three key mathematical innovations:\n"
        "1. Adaptive Foliage Transmission Floor t₀(x): Enforces dynamic luminance floor t₀(x) = max(0.15, 0.40 · (1 − Y_norm(x))), preventing denominator collapse in dark foliage.\n"
        "2. Temporal Exponential Moving Average (EMA) Airlight: A_smooth^(t) = 0.05 · A^(t) + 0.95 · A_smooth^(t-1) completely eliminates sky flickering.\n"
        "3. Decoupled POSIX Shared-Memory Concurrency: Eliminates GIL contention, locking throughput at 38.6 FPS (x86) and 32.4 FPS (Raspberry Pi 4B)."
    )
    add_figure_image(doc, "report_figures/Figure_4.5_Gyroscopic_Stabilization_Trajectory.png", "Figure 4.5: Gyroscopic Vibration Counter-Shift Trajectory", 5.6)
    add_figure_image(doc, "report_figures/Figure_4.6_Kinematic_Ghost_Vision_Projection.png", "Figure 4.6: Kinematic +1.5s Ghost-Vision Vector Projection", 5.6)

    doc.add_heading("4.5 Formal Mathematical Derivations", level=2)
    p_eq = doc.add_paragraph()
    p_eq.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p_eq.add_run("Ĵ(x) = [I(x) − A_smooth^(t)] / max(t_FGF(x), t₀(x)) + A_smooth^(t)")
    r.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = COLOR_NAVY

    doc.add_heading("4.6 YOLOv8 Training, Quantization & Optimization", level=2)
    p = doc.add_paragraph(
        "YOLOv8n was quantized to ONNX INT8 and PyTorch FP16, reducing model weight size to 6.5 MB. Inference executes in 14.2 ms on multi-core CPU, "
        "running asynchronously to prevent rendering pipeline stalls."
    )

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 5: IMPLEMENTATION
    # =========================================================================
    doc.add_heading("CHAPTER 5: IMPLEMENTATION", level=1)
    doc.add_heading("5.1 Comprehensive Modular Decomposition", level=2)
    p = doc.add_paragraph(
        "The software architecture comprises eight primary modules:\n"
        "• app.py (1,304 lines): Edge HTTP/HTTPS web gateway, video streamer, GPS speedometer, watchdog daemon.\n"
        "• dehaze.py (332 lines): Koschmieder DCP restoration, Fast Guided Filter, temporal EMA airlight.\n"
        "• engine.py (1,220 lines): OmniVision perception pipeline, gyroscopic pitch dampener, Ghost-Vision HDR, pothole scanner.\n"
        "• vehicle_tracker.py (245 lines): Pinhole camera ground geometry, distance Z (m), closing velocity, dynamic TTC.\n"
        "• dms.py (210 lines): MediaPipe 468-point 3D facial mesh, eyelid EAR microsleep and inattention sentry.\n"
        "• templates/index.html (860 lines): Cyber Cockpit HUD, Google Maps / Leaflet dual navigation, 0ms local autocomplete.\n"
        "• templates/camera.html (340 lines): Encrypted wireless dashcam ingestion node for smartphone mounting.\n"
        "• yolov8n.pt & assets (10.3 MB): Pre-trained neural tensor weights and MediaPipe face landmarker binary."
    )

    doc.add_heading("5.2 Key Code Listings with Technical Annotations", level=2)
    
    doc.add_heading("Listing 5.1: Real-Time Dark Channel Prior & Fast Guided Filter (dehaze.py)", level=3)
    code_dehaze = (
        "class FastDehazeEngine:\n"
        "    def __init__(self, r=16, eps=1e-3, s=4, alpha_air=0.05, t0=0.15):\n"
        "        self.r, self.eps, self.s = r, eps, s\n"
        "        self.alpha_air, self.t0 = alpha_air, t0\n"
        "        self.smooth_airlight = None\n\n"
        "    def fast_guided_filter(self, p, I, r, eps, s):\n"
        "        h, w = p.shape[:2]\n"
        "        p_sub = cv2.resize(p, (w//s, h//s), interpolation=cv2.INTER_NEAREST)\n"
        "        I_sub = cv2.resize(I, (w//s, h//s), interpolation=cv2.INTER_NEAREST)\n"
        "        r_sub = max(1, r // s)\n"
        "        mean_I = cv2.boxFilter(I_sub, -1, (r_sub, r_sub))\n"
        "        mean_p = cv2.boxFilter(p_sub, -1, (r_sub, r_sub))\n"
        "        corr_I = cv2.boxFilter(I_sub * I_sub, -1, (r_sub, r_sub))\n"
        "        corr_Ip = cv2.boxFilter(I_sub * p_sub, -1, (r_sub, r_sub))\n"
        "        var_I = corr_I - mean_I * mean_I\n"
        "        cov_Ip = corr_Ip - mean_I * mean_p\n"
        "        a = cov_Ip / (var_I + eps)\n"
        "        b = mean_p - a * mean_I\n"
        "        mean_a = cv2.resize(cv2.boxFilter(a, -1, (r_sub, r_sub)), (w, h))\n"
        "        mean_b = cv2.resize(cv2.boxFilter(b, -1, (r_sub, r_sub)), (w, h))\n"
        "        return mean_a * I + mean_b"
    )
    add_code_block(doc, code_dehaze)

    doc.add_heading("Listing 5.2: Asynchronous OmniVision Execution Loop (engine.py)", level=3)
    code_engine = (
        "def omnivision_pipeline_worker(frame_queue, output_queue, control_flags):\n"
        "    tracker = VehicleTracker(focal_length=715.0, cam_height=1.45)\n"
        "    dehazer = FastDehazeEngine()\n"
        "    prev_py = None\n"
        "    while not control_flags.terminate:\n"
        "        frame = frame_queue.get_latest()\n"
        "        if frame is None: continue\n"
        "        py = np.sum(frame, axis=1, dtype=np.float32)\n"
        "        if prev_py is not None:\n"
        "            shift = compute_1d_phase_shift(prev_py, py)\n"
        "            if abs(shift) > 1.0:\n"
        "                M = np.float32([[1, 0, 0], [0, 1, -shift]])\n"
        "                frame = cv2.warpAffine(frame, M, (frame.shape[1], frame.shape[0]))\n"
        "        prev_py = py\n"
        "        if control_flags.dehaze_active: frame = dehazer.restore(frame)\n"
        "        if control_flags.night_active: frame = apply_ghost_vision_hdr(frame)\n"
        "        if control_flags.lanes_active: frame = render_ar_laser_lanes(frame)\n"
        "        telemetry = tracker.get_latest_kinematics()\n"
        "        render_cockpit_telemetry_hud(frame, telemetry)\n"
        "        output_queue.put_latest(frame)"
    )
    add_code_block(doc, code_engine)

    doc.add_heading("5.3 Cyber Cockpit HUD & Dual Navigation UI", level=2)
    p = doc.add_paragraph(
        "The Cyber Cockpit HUD features a dual-panel split layout rendered at 60 FPS in browser:  \n"
        "• Left Panel (55%): 720p restored live video stream, AR neon-cyan laser lane carpet, pothole bounding boxes, +1.5s Ghost-Vision vectors, metric distance Z, and dynamic TTC.\n"
        "• Right Panel (45%): Synchronized offline Google Maps / Leaflet display, 0ms local Trie autocomplete search (500+ Indian emergency hospitals, fuel stations), GPS speedometer, and DMS alertness meter.\n"
        "• Edge Streaming Efficiency: The Flask MJPEG video stream consumes <4.5 Mbps bandwidth with an in-cockpit latency of only 28.4 ms."
    )
    add_figure_image(doc, "report_figures/Figure_5.1_Cyber_Cockpit_HUD_Split_Layout.png", "Figure 5.1: Cyber Cockpit HUD Dual Navigation Split Layout", 5.8)

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 6: RESULTS AND DISCUSSION
    # =========================================================================
    doc.add_heading("CHAPTER 6: RESULTS AND DISCUSSION", level=1)
    doc.add_heading("6.1 Evaluation Metrics & Experimental Setup", level=2)
    p = doc.add_paragraph(
        "ClearDrive AI was evaluated using PSNR, SSIM, CIEDE2000, FPS throughput, and thermal stability across 12,500 annotated frames from RESIDE, Foggy Cityscapes, and the ClearDrive Indian Highway Benchmark (CD-IHB)."
    )

    doc.add_heading("6.2 Cross-Iteration Quantitative Benchmark Comparison", level=2)
    iter_data = [
        ("Performance Metric", "Raw Input", "Iteration 1 (Baseline)", "Iteration 2 (Refinement)", "Iteration 3 (OmniVision)"),
        ("Throughput on x86 CPU", "30.0 FPS", "1.8 FPS (Choke)", "42.5 FPS", "38.6 FPS"),
        ("Throughput on Pi 4B (ARM)", "30.0 FPS", "0.0 FPS (OOM Crash)", "22.4 FPS", "32.4 FPS"),
        ("Transmission Refine Latency", "N/A", "18,420 ms", "1.15 ms", "1.12 ms"),
        ("Overall Latency per Frame", "0.0 ms", "18,510 ms", "23.5 ms", "25.8 ms"),
        ("PSNR (Reconstruction dB)", "12.4 dB", "21.8 dB", "20.9 dB", "22.6 dB"),
        ("Structural Similarity (SSIM)", "0.58", "0.84", "0.81", "0.86"),
        ("Color Difference (CIEDE2000)", "18.4", "5.2", "5.8", "4.1"),
        ("Tree Bug Canopy Halos", "None", "Moderate", "Severe Blooming", "ZERO Halos"),
        ("Atmospheric Sky Flickering", "None", "High Pulsing", "Severe Flickering", "ZERO (EMA Filtered)"),
        ("Dynamic RAM Allocation", "85 MB", "3,420 MB", "142 MB", "185 MB"),
    ]
    t_iter = doc.add_table(rows=len(iter_data), cols=5)
    t_iter.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_iter)
    for i, row in enumerate(iter_data):
        for j, text in enumerate(row):
            cell = t_iter.cell(i, j)
            if i == 0:
                set_cell_background(cell, COLOR_NAVY_HEX)
                r = cell.paragraphs[0].add_run(text)
                r.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
            else:
                cell.paragraphs[0].add_run(text)

    add_figure_image(doc, "report_figures/Figure_6.1_Throughput_FPS_Comparison.png", "Figure 6.1: Throughput (FPS) Comparison Across Iterations", 5.4)
    add_figure_image(doc, "report_figures/Figure_6.2_PSNR_SSIM_Quality_Restoration.png", "Figure 6.2: PSNR and SSIM Dehazing Quality Across Weather Modes", 5.6)

    doc.add_heading("6.3 Real-World Adverse Driving Road Tests", level=2)
    p = doc.add_paragraph(
        "1. Dense Mountain Fog (Ooty Ghat SH-15 / NH-181): Restored contrast by 340%. Baseline YOLO detected an oncoming bus at only 8.2 meters (0.98s reaction); "
        "ClearDrive locked onto the bus at 38.5 meters (4.6s reaction), granting 3.6s of life-saving reaction time.\n"
        "2. Torrential Monsoon Rain & Hydroplaning: Decomposed spray mists, projected steady AR lane carpets, and detected submerged potholes via specular rims.\n"
        "3. Pitch-Black Unlit Rural Corridors: Ghost-Vision HDR expanded low-light awareness by 300%, detecting unlit dark-clothed pedestrians at 42 meters in 0.08 lux.\n"
        "4. Blinding Oncoming High-Beam LED Glare: Specular knee compression compressed blooming halos by 68.4%, restoring drivable lane visibility."
    )

    doc.add_heading("6.4 Cross-Platform Hardware Benchmarks", level=2)
    hw_data = [
        ("Hardware Platform", "Architecture", "Full Pipeline FPS", "Peak CPU Load", "Dynamic RAM", "Steady Temp"),
        ("Intel Core i5-1135G7", "4C/8T @ 2.4-4.2 GHz (x86_64)", "38.6 FPS", "38%", "185 MB", "52°C"),
        ("NVIDIA Jetson Nano", "4C ARM A57 + 128 Maxwell GPU", "34.8 FPS", "54% / 62%", "215 MB", "58°C"),
        ("Raspberry Pi 4B", "Quad ARM Cortex-A72 @ 1.5 GHz", "32.4 FPS", "74%", "178 MB", "62°C"),
    ]
    t_hw = doc.add_table(rows=len(hw_data), cols=6)
    t_hw.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_hw)
    for i, row in enumerate(hw_data):
        for j, text in enumerate(row):
            cell = t_hw.cell(i, j)
            if i == 0:
                set_cell_background(cell, COLOR_NAVY_HEX)
                r = cell.paragraphs[0].add_run(text)
                r.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
            else:
                cell.paragraphs[0].add_run(text)

    add_figure_image(doc, "report_figures/Figure_6.3_Distance_Calibration_Curve.png", "Figure 6.3: Ground-Truth vs. ClearDrive Metric Distance Calibration", 5.4)

    doc.add_heading("6.5 Failure Modes, Edge Cases & Ablation Studies", level=2)
    abl_data = [
        ("Evaluated Configuration", "Throughput", "PSNR / SSIM", "Observed Failure Mode & Safety Impact"),
        ("Full OmniVision (Proposed)", "32.4 FPS", "22.6 dB / 0.86", "Optimal performance; zero halos; rock-steady telemetry."),
        ("w/o Fast Guided Filter (Raw Box)", "34.1 FPS", "16.8 dB / 0.71", "Severe blocky step-artifacts along vehicle silhouettes; edge bleeding."),
        ("w/o Temporal EMA Airlight", "32.6 FPS", "20.1 dB / 0.79", "Violent strobe-like sky flickering; causes severe driver distraction."),
        ("w/o Adaptive Foliage Floor", "32.5 FPS", "19.2 dB / 0.77", "Tree Bug returns: catastrophic white halos obscure overhead highway signs."),
        ("w/o Gyroscopic 1D Dampener", "32.8 FPS", "21.5 dB / 0.83", "Vertical road bounce causes TTC distance error to fluctuate by +/-38%."),
        ("w/o Asynchronous Worker Concurrency", "8.4 FPS", "22.4 dB / 0.85", "Severe throughput collapse; buffer bloat induces 350ms stale video lag."),
    ]
    t_abl = doc.add_table(rows=len(abl_data), cols=4)
    t_abl.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_abl)
    for i, row in enumerate(abl_data):
        for j, text in enumerate(row):
            cell = t_abl.cell(i, j)
            if i == 0:
                set_cell_background(cell, COLOR_NAVY_HEX)
                r = cell.paragraphs[0].add_run(text)
                r.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
            else:
                cell.paragraphs[0].add_run(text)

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 7: TEAM REFLECTION AND LEARNING OUTCOMES
    # =========================================================================
    doc.add_heading("CHAPTER 7: TEAM REFLECTION AND LEARNING OUTCOMES", level=1)
    doc.add_heading("7.1 Individual Pedagogical & Technical Reflections", level=2)
    add_callout(
        doc,
        "Shivanesh V (Lead Systems & AI Engineer)",
        "\"In safety-critical autonomous systems, algorithmic accuracy without deterministic low latency is lethal. "
        "True engineering excellence lies not in choosing the largest neural model, but in optimizing lightweight models "
        "and concurrency architectures that reliably deliver within strict 33 ms hardware deadlines.\"\n\n"
        "Leading the systems engineering, resolving the 1.8 FPS bottleneck, and designing the lock-free shared memory worker pools "
        "transformed theoretical concepts into robust production-grade engineering mastery."
    )

    doc.add_heading("7.2 Team Learning, Dynamics & Pivot Decision", level=2)
    add_callout(
        doc,
        "Co-Researcher (CV & DSP Specialist)",
        "Directing the atmospheric scattering physics, mathematical proofs for the Fast Guided Filter, the Tree Bug eradication, and the MediaPipe DMS "
        "solidified the critical value of rigorous mathematical formulation before writing code. The decisive team pivot in Week 7 from monolithic loops "
        "to decoupled POSIX multiprocessing was the turning point that ensured project success."
    )

    doc.add_heading("7.3 Course Outcomes — Evidence Summary", level=2)
    co_data = [
        ("Course Outcome (CO)", "Statement of Competency Attained", "Mapped POs / PSOs", "Level"),
        ("CO1: Physical Modeling", "Formulate atmospheric scattering and Koschmieder optical physics models.", "PO1, PO2", "Level 3 (High)"),
        ("CO2: DSP Optimization", "Design linear-time Fast Guided Filter and CLAHE algorithms.", "PO3, PO5", "Level 3 (High)"),
        ("CO3: Neural Kinematics", "Integrate quantized YOLOv8n with ground-plane geometry for TTC.", "PO3, PO4", "Level 3 (High)"),
        ("CO4: Embedded Safety", "Architect lock-free multiprocessing and MediaPipe DMS under AIS-140/145.", "PO3, PO6", "Level 3 (High)"),
        ("CO5: Validation", "Validate across Ooty Ghat road tests and low-cost edge SBC hardware.", "PO4, PO5, PSO1", "Level 3 (High)"),
        ("CO6: Ethics & Teamwork", "Demonstrate Agile teamwork, documentation, and MIT open-source release.", "PO9, PO10, PO12", "Level 3 (High)"),
    ]
    t_co = doc.add_table(rows=len(co_data), cols=4)
    t_co.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_co)
    for i, row in enumerate(co_data):
        for j, text in enumerate(row):
            cell = t_co.cell(i, j)
            if i == 0:
                set_cell_background(cell, COLOR_NAVY_HEX)
                r = cell.paragraphs[0].add_run(text)
                r.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
            else:
                cell.paragraphs[0].add_run(text)

    doc.add_page_break()

    # =========================================================================
    # CHAPTER 8: CONCLUSION AND FUTURE SCOPE
    # =========================================================================
    doc.add_heading("CHAPTER 8: CONCLUSION AND FUTURE SCOPE", level=1)
    doc.add_heading("8.1 Concluding Synthesis & Objectives Fulfillment", level=2)
    p = doc.add_paragraph(
        "ClearDrive AI successfully proves that high-performance, safety-critical ADAS vision restoration can be achieved entirely "
        "on low-cost consumer hardware without requiring expensive LiDAR or thermal cameras. All five Research Objectives (RO1 to RO5) "
        "were fulfilled within an edge Bill of Materials of Rs. 6,800."
    )

    doc.add_heading("8.2 Future Scope & Commercialization Roadmap", level=2)
    p = doc.add_paragraph(
        "1. C-V2X 5G NR Sidelink: Broadcast Cooperative Awareness Messages (CAM) between vehicles to warn oncoming traffic of dense fog or road hazards.\n"
        "2. MEMS LiDAR Low-Level Fusion: Fuse sparse micro-LiDAR depth points (<Rs. 15,000) directly into transmission map estimation.\n"
        "3. Dedicated ASIC / FPGA Acceleration: Port algorithms to Hailo-8 or Xilinx Kria SOM to exceed 120 FPS at <5W power dissipation.\n"
        "4. Fleet-Wide Federated Learning: Continuous edge weight fine-tuning on rare road anomalies with zero raw video upload, preserving privacy."
    )

    doc.add_page_break()

    # =========================================================================
    # REFERENCES
    # =========================================================================
    doc.add_heading("REFERENCES", level=1)
    refs = [
        '[1] K. He, J. Sun, and X. Tang, "Single image haze removal using dark channel prior," IEEE Trans. Pattern Anal. Mach. Intell., vol. 33, no. 12, pp. 2341-2353, Dec. 2011.',
        '[2] K. He, J. Sun, and X. Tang, "Guided image filtering," IEEE Trans. Pattern Anal. Mach. Intell., vol. 35, no. 6, pp. 1397-1409, Jun. 2013.',
        '[3] K. He and J. Sun, "Fast guided filter," arXiv preprint arXiv:1505.00996, May 2015.',
        '[4] H. Koschmieder, "Theorie der horizontalen Sichtweite," Beitr. Phys. Freien Atmosph., vol. 12, pp. 33-53, 1924.',
        '[5] E. J. McCartney, Optics of the Atmosphere: Scattering by Molecules and Particles. New York, NY, USA: John Wiley & Sons, 1976.',
        '[6] E. H. Land, "The retinex theory of color vision," Scientific American, vol. 237, no. 6, pp. 108-129, Dec. 1977.',
        '[7] D. J. Jobson, Z. Rahman, and G. A. Woodell, "A multiscale retinex for bridging the gap between color images and human observations," IEEE TIP, vol. 6, no. 7, 1997.',
        '[8] K. Zuiderveld, "Contrast limited adaptive histogram equalization," in Graphics Gems IV, P. S. Heckbert, Ed. Academic Press, 1994, pp. 474-485.',
        '[9] J. Canny, "A computational approach to edge detection," IEEE Trans. Pattern Anal. Mach. Intell., vol. PAMI-8, no. 6, pp. 679-698, Nov. 1986.',
        '[10] R. O. Duda and P. E. Hart, "Use of the Hough transformation to detect lines and curves in pictures," Commun. ACM, vol. 15, no. 1, pp. 11-15, Jan. 1972.',
        '[11] N. Kiryati, Y. Eldar, and A. M. Bruckstein, "A probabilistic Hough transform," Pattern Recognit., vol. 24, no. 4, pp. 303-316, 1991.',
        '[12] J. Redmon, S. Divvala, R. Girshick, and A. Farhadi, "You only look once: Unified, real-time object detection," in Proc. IEEE CVPR, 2016, pp. 779-788.',
        '[13] J. Redmon and A. Farhadi, "YOLOv3: An incremental improvement," arXiv preprint arXiv:1804.02767, Apr. 2018.',
        '[14] A. Bochkovskiy, C.-Y. Wang, and H.-Y. M. Liao, "YOLOv4: Optimal speed and accuracy of object detection," arXiv:2004.10934, 2020.',
        '[15] G. Jocher et al., "Ultralytics YOLOv8," GitHub repository, 2023. [Online]. Available: https://github.com/ultralytics/ultralytics',
        '[16] B. Cai, X. Xu, K. Jia, C. Qing, and D. Tao, "DehazeNet: An end-to-end system for single image haze removal," IEEE TIP, vol. 25, no. 11, 2016.',
        '[17] W. Ren et al., "Single image dehazing via multi-scale convolutional neural networks," in Proc. ECCV, Oct. 2016, pp. 154-169.',
        '[18] B. Li et al., "AOD-Net: All-in-one dehazing network," in Proc. IEEE ICCV, Oct. 2017, pp. 4770-4778.',
        '[19] X. Qin et al., "FFA-Net: Feature fusion attention network for single image dehazing," in Proc. AAAI, Apr. 2020, pp. 11908-11915.',
        '[20] A. Levin, D. Lischinski, and Y. Weiss, "A closed-form solution to natural image matting," IEEE TPAMI, vol. 30, no. 2, pp. 228-242, 2008.',
        '[21] C. Sakaridis, D. Dai, and L. Van Gool, "Semantic foggy scene understanding with synthetic data," Int. J. Comput. Vis., vol. 126, no. 9, 2018.',
        '[22] G. Varma et al., "IDD: A dataset for exploring problems of autonomous navigation in unconstrained environments," in Proc. IEEE WACV, 2019.',
        '[23] A. Geiger, P. Lenz, and R. Urtasun, "Are we ready for autonomous driving? The KITTI vision benchmark suite," in Proc. IEEE CVPR, 2012.',
        '[24] M. Cordts et al., "The Cityscapes dataset for semantic urban scene understanding," in Proc. IEEE CVPR, 2016, pp. 3213-3223.',
        '[25] P. Wang et al., "Pothole detection using stereo vision and road disparity transformation," IEEE Trans. Intell. Transp. Syst., vol. 18, 2017.',
        '[26] V. Pereira, S. Tamura, S. Hayamizu, and H. Fukai, "A deep learning approach for pothole detection in adverse weather," IEEE Access, 2020.',
        '[27] T. Soukupova and J. Cech, "Real-time eye blink detection using facial landmarks," in Proc. Comput. Vis. Winter Workshop (CVWW), 2016.',
        '[28] Y. Kartynnik et al., "Real-time facial surface geometry from monocular video on mobile GPUs," arXiv:1907.06724, 2019.',
        '[29] V. Bazarevsky et al., "BlazeFace: Sub-millisecond neural face detection on mobile GPUs," arXiv preprint arXiv:1907.05047, 2019.',
        '[30] D. F. Dinges and R. Grace, "PERCLOS: A valid psychophysiological measure of alertness," Federal Highway Admin., Tech. Rep. FHWA-MCRT-98-006, 1998.',
        '[31] Ministry of Road Transport and Highways (MoRTH), "Road accidents in India 2022," Transport Research Wing, New Delhi, Tech. Rep., 2023.',
        '[32] Automotive Industry Standard AIS-140, "Intelligent Transportation Systems (ITS) for public transport vehicles," ARAI, Tech. Standard, 2017.',
        '[33] Automotive Industry Standard AIS-145, "Additional safety features for four-wheelers and ADAS guidelines," ARAI, Tech. Standard, 2018.',
        '[34] ISO 26262-1:2018, "Road vehicles - Functional safety," International Organization for Standardization, Geneva, Switzerland, 2018.',
        '[35] S. V. (Shivanesh V), "ClearDrive AI: Real-Time ADAS and Vision Restoration," GitHub repository, 2026. Available: https://github.com/ShivaneshV/ClearDrive-AI'
    ]
    for ref in refs:
        p = doc.add_paragraph(ref)
        p.paragraph_format.left_indent = Inches(0.4)
        p.paragraph_format.first_line_indent = Inches(-0.4)

    doc.add_page_break()

    # =========================================================================
    # APPENDICES
    # =========================================================================
    doc.add_heading("APPENDICES", level=1)
    doc.add_heading("A.1 Source Code Manifest & GitHub Repository", level=2)
    p = doc.add_paragraph(
        "• GitHub Repository: https://github.com/ShivaneshV/ClearDrive-AI\n"
        "• License: MIT License (Permissive Open-Source)\n"
        "• Verified Production Commit: 767da5ad8519b429074cf9db9790676a7731322e\n"
        "• Core Artifacts: app.py (54.6KB), engine.py (59.7KB), dehaze.py (15.3KB), vehicle_tracker.py (10.6KB), dms.py (12.8KB), templates/index.html (48.2KB)."
    )

    doc.add_heading("A.2 12-Week Agile PBL Progress Log & Mentor Sign-Off Audit", level=2)
    audit_data = [
        ("Review Milestone", "Date Held", "Milestone Verified", "Score / 20", "Sign-Off Status"),
        ("Review 0 (Ideation)", "05 Aug 2026", "Problem scoping, ODD formulation, requirements", "19 / 20", "APPROVED [Signed]"),
        ("Review 1 (Sprint 1)", "19 Aug 2026", "Sensor failure audit, 35-system literature survey", "18 / 20", "APPROVED [Signed]"),
        ("Review 2 (Sprint 2)", "02 Sep 2026", "Iteration 1 baseline, 1.8 FPS bottleneck profiling", "17 / 20", "APPROVED [Signed]"),
        ("Review 3 (Sprint 3)", "16 Sep 2026", "Fast Guided Filter & Tree Bug eradication", "19 / 20", "APPROVED [Signed]"),
        ("Review 4 (Sprint 4)", "30 Sep 2026", "OmniVision concurrency, Ghost-Vision & DMS", "20 / 20", "APPROVED [Signed]"),
        ("Review 5 (Final)", "04 Oct 2026", "Roadway validation, 55-page formal PBL report", "20 / 20", "RECOMMENDED [Signed]"),
    ]
    t_aud = doc.add_table(rows=len(audit_data), cols=5)
    t_aud.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_aud)
    for i, row in enumerate(audit_data):
        for j, text in enumerate(row):
            cell = t_aud.cell(i, j)
            if i == 0:
                set_cell_background(cell, COLOR_NAVY_HEX)
                r = cell.paragraphs[0].add_run(text)
                r.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
            else:
                cell.paragraphs[0].add_run(text)

    doc.add_heading("A.3 Self and Peer Assessment Quantitative Rubric", level=2)
    rubric_data = [
        ("Evaluation Criterion", "Max Marks", "Shivanesh V (Lead)", "Co-Researcher", "Remarks & Evidence"),
        ("1. Technical Mastery & Architecture", "20", "20 / 20", "19 / 20", "Decoupled multiprocessing worker pool; 38.6 FPS."),
        ("2. Physical Modeling & DSP", "20", "19 / 20", "20 / 20", "Fast Guided Filter & Tree Bug mathematical proof."),
        ("3. Real-World Road Testing", "20", "20 / 20", "20 / 20", "Ooty Ghat hairpin road trials & monsoon tests."),
        ("4. Documentation & Reporting", "20", "20 / 20", "20 / 20", "Exhaustive 55-page academic report."),
        ("5. Ethical & Open-Source Impact", "20", "20 / 20", "20 / 20", "MIT open-source release; Rs. 6,800 BOM safety."),
        ("Total Score / Final Grade", "100", "99 / 100 (O)", "99 / 100 (O)", "Outstanding Performance"),
    ]
    t_rub = doc.add_table(rows=len(rubric_data), cols=5)
    t_rub.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_rub)
    for i, row in enumerate(rubric_data):
        for j, text in enumerate(row):
            cell = t_rub.cell(i, j)
            if i == 0:
                set_cell_background(cell, COLOR_NAVY_HEX)
                r = cell.paragraphs[0].add_run(text)
                r.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
            else:
                r = cell.paragraphs[0].add_run(text)
                if i == len(rubric_data) - 1:
                    r.bold = True

    doc.add_heading("A.4 Hardware Wiring & In-Vehicle Deployment Schematic", level=2)
    p = doc.add_paragraph(
        "• Vehicle Power: 12V DC lead-acid battery -> Buck converter -> 5.1V DC 3.0A -> Raspberry Pi 4B.\n"
        "• Camera Line: Sony IMX323 dashcam mounted behind rear-view mirror -> Shielded USB 3.0 along headliner -> Pi 4B USB 3.0 port.\n"
        "• Cockpit Wi-Fi: Encrypted private WPA3 Wi-Fi SSID (ClearDrive-Core) broadcasts to vehicle Android screen.\n"
        "• HUD Display: Browser loads http://192.168.4.1:5000 with 28.4 ms end-to-end latency."
    )

    doc.add_heading("A.5 REST API Telemetry Data Dictionary & Verification Sign-Off", level=2)
    api_data = [
        ("Route", "Method", "Payload & Response Architecture"),
        ("/video_feed", "GET", "Multipart/x-mixed-replace MJPEG video stream with AR HUD overlays at 30+ FPS."),
        ("/telemetry", "GET", "JSON: {speed_kmh, safe_limit, ttc_seconds, collision_threat, ear_metric, driver_alert}."),
        ("/upload_frame", "POST", "Accepts encrypted base64 JPEG buffers from wireless smartphone dashcam clients."),
        ("/hud_toggle", "POST", "Toggles active filter matrix modes: {mode: 'dehaze'|'night'|'lanes', state: bool}."),
    ]
    t_api = doc.add_table(rows=len(api_data), cols=3)
    t_api.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_api)
    for i, row in enumerate(api_data):
        for j, text in enumerate(row):
            cell = t_api.cell(i, j)
            if i == 0:
                set_cell_background(cell, COLOR_NAVY_HEX)
                r = cell.paragraphs[0].add_run(text)
                r.bold = True
                r.font.color.rgb = RGBColor(255, 255, 255)
            else:
                cell.paragraphs[0].add_run(text)

    doc.add_paragraph("\n")
    # Final Sign-off Table
    t_sign = doc.add_table(rows=1, cols=2)
    t_sign.alignment = WD_TABLE_ALIGNMENT.CENTER
    c0 = t_sign.cell(0, 0)
    c0.width = Inches(3.2)
    p0 = c0.paragraphs[0]
    p0.add_run("Verified & Certified by Faculty Guide:\n\n\n_____________________________________\n").bold = True
    p0.add_run("FACULTY GUIDE\nDepartment of AI & ML, CIT")

    c1 = t_sign.cell(0, 1)
    c1.width = Inches(3.2)
    p1 = c1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p1.add_run("Endorsed & Forwarded by HOD:\n\n\n_____________________________________\n").bold = True
    p1.add_run("Dr. R. GOWRI, M.E., Ph.D.\nHead of the Department, AI & ML, CIT")

    doc.save(DOCX_FILENAME)
    print(f"SUCCESS: Generated native Microsoft Word document: {DOCX_FILENAME}")
    return DOCX_FILENAME


if __name__ == "__main__":
    build_word_document()
