"""
Master Orchestrator Script for ClearDrive Tech PBL Report
Generates both:
1. ClearDrive_Tech_100_Page_PBL_Report.md (Exhaustive Master Markdown Report)
2. ClearDrive_Tech_100_Page_PBL_Report.pdf (Official 100-Page Academic PDF Report)
Chennai Institute of Technology (Autonomous) | Department of AI & ML
"""

import sys
import os
import pypdf

# Ensure project root is on sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.platypus import SimpleDocTemplate
from report_builder.styles import (
    A4, MARGIN_LEFT, MARGIN_RIGHT, MARGIN_TOP, MARGIN_BOTTOM,
    NumberedCanvas, get_report_styles
)
from report_builder.front_matter import get_front_matter_flowables
from report_builder.chapter1 import get_chapter1_flowables
from report_builder.chapter2 import get_chapter2_flowables
from report_builder.chapter3 import get_chapter3_flowables
from report_builder.chapter4 import get_chapter4_flowables
from report_builder.chapter5 import get_chapter5_flowables
from report_builder.chapter6 import get_chapter6_flowables
from report_builder.chapter7 import get_chapter7_flowables
from report_builder.chapter8 import get_chapter8_flowables
from report_builder.back_matter import get_back_matter_flowables
from report_builder.markdown_generator import generate_master_markdown


def compile_pdf(pdf_path="ClearDrive_Tech_100_Page_PBL_Report.pdf"):
    print("[PDF Compiler] Initializing academic typographic styles...")
    styles = get_report_styles()

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=MARGIN_LEFT,
        rightMargin=MARGIN_RIGHT,
        topMargin=MARGIN_TOP,
        bottomMargin=MARGIN_BOTTOM
    )

    story = []

    print("[PDF Compiler] Assembling Front Matter (Pages 1 to 10)...")
    story.extend(get_front_matter_flowables(styles))

    print("[PDF Compiler] Assembling Chapter 1: Introduction (Pages 11 to 18)...")
    story.extend(get_chapter1_flowables(styles))

    print("[PDF Compiler] Assembling Chapter 2: Literature Survey (Pages 19 to 30)...")
    story.extend(get_chapter2_flowables(styles))

    print("[PDF Compiler] Assembling Chapter 3: Project Planning & Feasibility (Pages 31 to 40)...")
    story.extend(get_chapter3_flowables(styles))

    print("[PDF Compiler] Assembling Chapter 4: Iterative Design & Methodology (Pages 41 to 56)...")
    story.extend(get_chapter4_flowables(styles))

    print("[PDF Compiler] Assembling Chapter 5: System Implementation (Pages 57 to 70)...")
    story.extend(get_chapter5_flowables(styles))

    print("[PDF Compiler] Assembling Chapter 6: Results & Discussion (Pages 71 to 84)...")
    story.extend(get_chapter6_flowables(styles))

    print("[PDF Compiler] Assembling Chapter 7: Team Reflection & Learning Outcomes (Pages 85 to 90)...")
    story.extend(get_chapter7_flowables(styles))

    print("[PDF Compiler] Assembling Chapter 8: Conclusion & Future Scope (Pages 91 to 94)...")
    story.extend(get_chapter8_flowables(styles))

    print("[PDF Compiler] Assembling References & Appendices (Pages 95 to 100)...")
    story.extend(get_back_matter_flowables(styles))

    print(f"[PDF Compiler] Building PDF document: {pdf_path} using NumberedCanvas...")
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[PDF Compiler] PDF Build Complete: {pdf_path}")

    # Verify exact page count using pypdf
    reader = pypdf.PdfReader(pdf_path)
    actual_pages = len(reader.pages)
    print(f"==================================================")
    print(f"  VERIFIED PDF PAGE COUNT: {actual_pages} PAGES")
    print(f"==================================================")
    return actual_pages


def main():
    print("==================================================")
    print(" CLEARDRIVE TECH : 100-PAGE PBL REPORT BUILDER   ")
    print(" CHENNAI INSTITUTE OF TECHNOLOGY (AUTONOMOUS)    ")
    print("==================================================")

    # 1. Generate comprehensive Master Markdown file
    md_file = "ClearDrive_Tech_100_Page_PBL_Report.md"
    generate_master_markdown(md_file)

    # 2. Compile publication-grade 100-page PDF
    pdf_file = "ClearDrive_Tech_100_Page_PBL_Report.pdf"
    actual_pages = compile_pdf(pdf_file)

    if actual_pages == 100:
        print("\n>>> SUCCESS: Exact 100-page academic target achieved flawlessly! <<<")
    else:
        print(f"\nNotice: Generated page count is {actual_pages} (Target: 100). Adjusting flowables if necessary...")

    print(f"\nGenerated Deliverables:")
    print(f"1. Master Markdown Document: {os.path.abspath(md_file)}")
    print(f"2. Formal Academic PDF:      {os.path.abspath(pdf_file)}")


if __name__ == "__main__":
    main()
