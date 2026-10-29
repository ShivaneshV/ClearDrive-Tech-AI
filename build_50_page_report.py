"""
Master Orchestrator Script for ClearDrive AI 50-Page PBL Report
Department of Artificial Intelligence and Machine Learning
Chennai Institute of Technology (Autonomous) | Affiliated to Anna University, Chennai

Strict Rules Enforced:
- EXACTLY 50 Pages (Page 1 of 50 to Page 50 of 50)
- Zero Index Pages (NO Table of Contents, NO List of Figures, NO List of Tables, NO List of Abbreviations)
- Bonafide Content Alone: Title & Official Bonafide Certificate on Page 1, followed immediately by
  Chapter 1 to Chapter 8, References, and Appendices across Pages 2 to 50.
- Shortened Title: CLEARDRIVE AI: REAL-TIME ADAS AND VISION RESTORATION FOR ADVERSE DRIVING CONDITIONS
- Currency strictly formatted as 'Rs.' (Zero black box glyphs)
"""

import sys
import os
import pypdf

# Ensure project root is on sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.platypus import SimpleDocTemplate
from report_builder_50.styles import (
    A4, MARGIN_LEFT, MARGIN_RIGHT, MARGIN_TOP, MARGIN_BOTTOM,
    NumberedCanvas50, get_styles_50
)
from report_builder_50.page_01_bonafide import get_page_01_flowables
from report_builder_50.chapter1 import get_chapter1_flowables
from report_builder_50.chapter2 import get_chapter2_flowables
from report_builder_50.chapter3 import get_chapter3_flowables
from report_builder_50.chapter4 import get_chapter4_flowables
from report_builder_50.chapter5 import get_chapter5_flowables
from report_builder_50.chapter6 import get_chapter6_flowables
from report_builder_50.chapter7 import get_chapter7_flowables
from report_builder_50.chapter8 import get_chapter8_flowables
from report_builder_50.back_matter import get_back_matter_flowables
from report_builder_50.markdown_generator import generate_master_markdown


def compile_50_page_pdf(pdf_path="ClearDrive_AI_50_Page_PBL_Report.pdf"):
    print("[50p PDF Compiler] Initializing academic typographic styles...")
    styles = get_styles_50()

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=MARGIN_LEFT,
        rightMargin=MARGIN_RIGHT,
        topMargin=MARGIN_TOP,
        bottomMargin=MARGIN_BOTTOM
    )

    story = []

    print("[50p PDF Compiler] Assembling Page 1: Title & Bonafide Certificate...")
    story.extend(get_page_01_flowables(styles))

    print("[50p PDF Compiler] Assembling Chapter 1: Introduction (Pages 2 to 6)...")
    story.extend(get_chapter1_flowables(styles))

    print("[50p PDF Compiler] Assembling Chapter 2: Literature Survey (Pages 7 to 13)...")
    story.extend(get_chapter2_flowables(styles))

    print("[50p PDF Compiler] Assembling Chapter 3: Project Planning & Feasibility (Pages 14 to 18)...")
    story.extend(get_chapter3_flowables(styles))

    print("[50p PDF Compiler] Assembling Chapter 4: Iterative Design & Methodology (Pages 19 to 28)...")
    story.extend(get_chapter4_flowables(styles))

    print("[50p PDF Compiler] Assembling Chapter 5: System Implementation (Pages 29 to 35)...")
    story.extend(get_chapter5_flowables(styles))

    print("[50p PDF Compiler] Assembling Chapter 6: Results & Discussion (Pages 36 to 43)...")
    story.extend(get_chapter6_flowables(styles))

    print("[50p PDF Compiler] Assembling Chapter 7: Team Reflection & Learning Outcomes (Pages 44 to 46)...")
    story.extend(get_chapter7_flowables(styles))

    print("[50p PDF Compiler] Assembling Chapter 8: Conclusion & Future Scope (Pages 47 to 48)...")
    story.extend(get_chapter8_flowables(styles))

    print("[50p PDF Compiler] Assembling Back Matter: References & Appendices (Pages 49 to 50)...")
    story.extend(get_back_matter_flowables(styles))

    print(f"[50p PDF Compiler] Building PDF document: {pdf_path} using NumberedCanvas50...")
    doc.build(story, canvasmaker=NumberedCanvas50)
    print(f"[50p PDF Compiler] PDF Build Complete: {pdf_path}")

    # Verify exact page count using pypdf
    reader = pypdf.PdfReader(pdf_path)
    actual_pages = len(reader.pages)
    print(f"==================================================")
    print(f"  VERIFIED PDF PAGE COUNT: {actual_pages} PAGES")
    print(f"==================================================")
    return actual_pages


def main():
    print("==================================================")
    print(" CLEARDRIVE AI : 50-PAGE STRICT PBL REPORT BUILDER")
    print(" CHENNAI INSTITUTE OF TECHNOLOGY (AUTONOMOUS)    ")
    print("==================================================")

    # 1. Generate comprehensive Master Markdown file
    md_file = "ClearDrive_AI_50_Page_PBL_Report.md"
    generate_master_markdown(md_file)

    # 2. Compile publication-grade 50-page PDF
    pdf_file = "ClearDrive_AI_50_Page_PBL_Report.pdf"
    actual_pages = compile_50_page_pdf(pdf_file)

    if actual_pages == 50:
        print("\n>>> SUCCESS: Exact 50-page academic target achieved flawlessly! <<<")
    else:
        print(f"\nNotice: Generated page count is {actual_pages} (Target: 50).")

    print(f"\nGenerated Deliverables:")
    print(f"1. Master Markdown Document: {os.path.abspath(md_file)}")
    print(f"2. Formal Academic PDF:      {os.path.abspath(pdf_file)}")


if __name__ == "__main__":
    main()
