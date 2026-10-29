"""
ClearDrive AI: 55-Page Master Academic Report Builder
Chennai Institute of Technology (Autonomous) | Department of AI & ML
Strictly 55 Pages Verified via PyPDF.
"""

import sys
import os
import pypdf
from reportlab.platypus import SimpleDocTemplate
from report_builder_55.styles import get_styles_55, NumberedCanvas55
from report_builder_55.front_matter import get_front_matter_flowables
from report_builder_55.chapter1 import get_chapter1_flowables
from report_builder_55.chapter2 import get_chapter2_flowables
from report_builder_55.chapter3 import get_chapter3_flowables
from report_builder_55.chapter4 import get_chapter4_flowables
from report_builder_55.chapter5 import get_chapter5_flowables
from report_builder_55.chapter6 import get_chapter6_flowables
from report_builder_55.chapter7 import get_chapter7_flowables
from report_builder_55.chapter8 import get_chapter8_flowables
from report_builder_55.back_matter import get_back_matter_flowables

PDF_FILENAME = "ClearDrive_AI_55_Page_PBL_Report.pdf"


def build_55_page_report():
    print("=" * 70)
    print("BUILDING CLEARDRIVE AI 55-PAGE ACADEMIC REPORT")
    print("Chennai Institute of Technology | Dept. of AI & ML")
    print("=" * 70)

    doc = SimpleDocTemplate(
        PDF_FILENAME,
        pagesize=(595.27, 841.89),  # A4
        leftMargin=54,              # 0.75 in
        rightMargin=45,
        topMargin=50,
        bottomMargin=50
    )

    styles = get_styles_55()
    story = []

    print("[1/10] Loading Front Matter (Pages 1 - 5)...")
    story.extend(get_front_matter_flowables(styles))

    print("[2/10] Loading Chapter 1: Introduction (Pages 6 - 10)...")
    story.extend(get_chapter1_flowables(styles))

    print("[3/10] Loading Chapter 2: Literature Survey (Pages 11 - 17)...")
    story.extend(get_chapter2_flowables(styles))

    print("[4/10] Loading Chapter 3: Project Planning & Feasibility (Pages 18 - 22)...")
    story.extend(get_chapter3_flowables(styles))

    print("[5/10] Loading Chapter 4: Methodology (Pages 23 - 32)...")
    story.extend(get_chapter4_flowables(styles))

    print("[6/10] Loading Chapter 5: Implementation (Pages 33 - 39)...")
    story.extend(get_chapter5_flowables(styles))

    print("[7/10] Loading Chapter 6: Results & Discussion (Pages 40 - 47)...")
    story.extend(get_chapter6_flowables(styles))

    print("[8/10] Loading Chapter 7: Reflections & Outcomes (Pages 48 - 50)...")
    story.extend(get_chapter7_flowables(styles))

    print("[9/10] Loading Chapter 8: Conclusion & Future Scope (Pages 51 - 52)...")
    story.extend(get_chapter8_flowables(styles))

    print("[10/10] Loading References & Appendices (Pages 53 - 55)...")
    story.extend(get_back_matter_flowables(styles))

    print(f"\nCompiling PDF document with NumberedCanvas55...")
    doc.build(story, canvasmaker=NumberedCanvas55)

    # Verification with PyPDF
    reader = pypdf.PdfReader(PDF_FILENAME)
    total_pages = len(reader.pages)
    print("=" * 70)
    print(f"VERIFICATION RESULT: Generated PDF has {total_pages} pages.")
    print("=" * 70)

    if total_pages == 55:
        print("SUCCESS! The PDF matches the exact target of 55 pages.")
    else:
        print(f"WARNING: Expected exactly 55 pages, but got {total_pages} pages!")

    return total_pages


if __name__ == "__main__":
    count = build_55_page_report()
    sys.exit(0 if count == 55 else 1)
