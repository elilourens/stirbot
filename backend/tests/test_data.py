"""
Test dataset for RAGAS evaluation of the Stirling University RAG chatbot.
Ground truth answers sourced directly from Stirling University website.
50 diverse Q&A pairs covering admissions, fees, accommodation, campus life,
research, support services, and more.
"""
from datasets import Dataset

# Comprehensive test cases with real ground truth from Stirling University website
test_qa_pairs = {
    "question": [
        "How much does an undergraduate course cost for international students at Stirling University?",
        "What accommodation is available on the Stirling University campus?",
        "Where is Stirling University campus located?",
        "How many students study at Stirling University?",
        "What facilities are available in student accommodation?",
        "What is included in Stirling University accommodation rent?",
        "How many rooms does Stirling University accommodation have?",
        "What are the different types of accommodation available?",
        "Are there catering facilities on campus?",
        "How many nationalities are represented at Stirling University?",
        "What is the UCAS institution code for the University of Stirling?",
        "How many undergraduate courses does the University of Stirling offer?",
        "How many postgraduate degrees are available at the University of Stirling?",
        "What percentage of Stirling graduates are in employment or further study after graduation?",
        "When was the University of Stirling founded?",
        "How large is the University of Stirling campus?",
        "How many students study at the University of Stirling?",
        "What proportion of Stirling students are international, and how many nationalities are represented?",
        "How many staff members work at the University of Stirling?",
        "How many alumni does the University of Stirling have, and in how many countries?",
        "What are the University of Stirling's rankings in the major UK university guides?",
        "How did the University of Stirling perform in REF 2021?",
        "What percentage of University of Stirling research is rated world-leading or internationally excellent?",
        "Where does the University of Stirling rank for research impact in Agriculture, Veterinary and Food Science?",
        "What are the English language requirements for undergraduate study at the University of Stirling?",
        "What IELTS score is required for postgraduate study at the University of Stirling?",
        "What pre-sessional English language courses are available at the University of Stirling, and how much do they cost?",
        "What is the International Undergraduate Scholarship at Stirling and how much is it worth?",
        "What is the Vice Chancellor's Postgraduate International Scholarship at Stirling?",
        "Is there a scholarship for EU undergraduate students at the University of Stirling?",
        "What is the Stirling Success Scholarship and who is it for?",
        "Does the University of Stirling offer sports scholarships?",
        "What are the tuition fees for a PhD at the University of Stirling for UK/home students?",
        "What are the tuition fees for a PhD at the University of Stirling for international students?",
        "How many accommodation rooms does the University of Stirling offer?",
        "What is included in the University of Stirling accommodation rent?",
        "What is the cheapest on-campus accommodation available at the University of Stirling?",
        "Are first-year undergraduate students guaranteed accommodation at Stirling?",
        "How do students apply for University of Stirling accommodation?",
        "How much does a sport and fitness membership cost at the University of Stirling?",
        "What sport and fitness facilities are available at the University of Stirling?",
        "How does the University of Stirling rank for its sport facilities?",
        "How many clubs and societies are there at the University of Stirling?",
        "What is the University of Stirling Students' Union and how does it work?",
        "How many books does the University of Stirling library hold?",
        "What student support services are available at the University of Stirling?",
        "What are the estimated monthly living costs for a student at the University of Stirling?",
        "What are the entry requirements for a postgraduate taught degree at the University of Stirling?",
        "What documents are needed to apply for a postgraduate course at the University of Stirling?",
        "Is there a cinema or arts venue on the University of Stirling campus?",
    ],
    "ground_truth": [
        "International undergraduate tuition fees at Stirling University range from GBP 17,200 to GBP 23,700 per year, with specific fees varying by course. The university also offers scholarships ranging from GBP 2,000 to 4,000 per year to eligible students.",
        "Stirling University offers accommodation with over 2,800 rooms available right on the beautiful 330-acre campus, as well as easy-to-reach off-campus residences.",
        "Stirling University campus is set within 330 acres of grounds beneath the Ochil Hills, located 2 miles from the centre of Stirling in Scotland, close to the town of Bridge of Allan.",
        "The University of Stirling has 17,500+ students from 140+ nationalities studying globally. This includes 6,000 students in their growing postgraduate community. More than 30% of students come from an international background.",
        "University accommodation includes laundrettes. Although all accommodation is self-catered, on campus there is Refresh Bistro for breakfast, lunch or dinner, as well as other catering outlets across campus. All kitchens have a cooker, fridge, freezer, microwave and kettle.",
        "Utilities, Wi-Fi, room and contents insurance, bedding and bed linen, housekeeping assistance and 24/7 staff assistance are all included in the rent for University of Stirling accommodation.",
        "Stirling University accommodation has over 2,800 rooms available right on the campus.",
        "Stirling University offers different accommodation types: Shared Rooms are the most affordable with weekly rents ranging from £80 to £120, usually involving sharing a kitchen and bathroom. En-suite Rooms offer a private bathroom with shared kitchen facilities, costing between £120 and £180 per week.",
        "Yes, on campus there is Refresh Bistro for breakfast, lunch or dinner, as well as more than a dozen other restaurants and cafes across campus.",
        "Stirling University represents over 140 nationalities among its student population, with more than 30% of students coming from an international background.",
        "The University of Stirling's UCAS institution name is STIRL and its institution code is S75. The UCAS application fee for 2026 entry is £28.95 for up to five course choices, and the standard deadline for full-time undergraduate applications is 14 January 2026.",
        "The University of Stirling offers over 170 single and combined undergraduate courses. These are available in flexible degree formats with full-time September entry, as well as January entry and part-time options.",
        "The University of Stirling offers 90 postgraduate degrees, including MSc, MA, MRes, and MLitt qualifications. Most taught Masters courses take one year to complete. Research degrees include MPhil, PhD, and Professional Doctorates.",
        "93% of University of Stirling graduates were in employment or further study 15 months after graduation, according to the Graduate Outcomes survey 2022-23 (HESA). Faculty-specific positive destination rates ranged from 92.9% to 96.7%.",
        "The University of Stirling was founded in 1967. It was the first new university to be established in Scotland for nearly 400 years. The first intake of 164 undergraduate and 31 postgraduate students began their courses on 18 September 1967. Lord Robbins served as the university's first Chancellor.",
        "The University of Stirling campus covers approximately 330 acres (some sources cite 360 acres including the Innovation Park). The campus is set on the historic Airthrey estate, which includes the 18th-century Airthrey Castle designed by Robert Adam. In 2002 the estate was designated one of the UK's top 20 heritage sites of the 20th century by the International Council on Monuments and Sites.",
        "The University of Stirling has over 17,500 students globally, including more than 11,000 undergraduates and over 6,000 postgraduates. The university is organised into five faculties and employs approximately 1,500 staff.",
        "More than 30% of University of Stirling students are international, with over 140 nationalities represented on campus. The university is described as having a vibrant and supportive international learning environment.",
        "The University of Stirling employs approximately 1,500 staff members across its five faculties and professional services directorates.",
        "The University of Stirling has over 100,000 alumni (some sources cite 110,000+) living and working in 180 countries around the world.",
        "The University of Stirling is ranked 51st in the UK in the Complete University Guide 2026, and 55th overall in the Times and Sunday Times Good University Guide 2026. It is also ranked in the top 200 globally for UN Sustainable Development Goals (Times Higher Education 2025) and 177th worldwide in the QS World Sustainability Rankings. Subject rankings include 1st in Scotland and 1st in the UK for Heritage Studies, 1st in Scotland and 2nd in the UK for Paramedic Science, and 1st in Scotland for Criminology.",
        "In REF 2021, the University of Stirling ranked joint 4th in Scotland and joint 43rd in the UK for research impact (Times Higher Education rankings). The university improved across all three assessment pillars between REF 2014 and REF 2021. Its Institute of Aquaculture ranked 1st in the UK in Agriculture, Veterinary and Food Science for impact, with 100% of its research achieving outstanding impact.",
        "80.74% of University of Stirling research is rated as world-leading or internationally excellent (up from 71.9% in REF 2014). 87.05% of its research is deemed to have outstanding or very considerable impact on society (up from 82.6% in 2014). The research environment scored 85% at world-leading/internationally excellent level (up from 78.1% in 2014).",
        "The University of Stirling's Institute of Aquaculture ranked 1st in the UK for research impact in Agriculture, Veterinary and Food Science in REF 2021, with 100% of its research rated at the highest possible level of outstanding impact. The university is also top 15 in the UK for Geography and Environmental Studies research impact.",
        "For undergraduate study, international students whose first language is not English typically need IELTS Academic 6.0 overall with no sub-skill below 5.5. Equivalent scores are also accepted: TOEFL iBT 80 overall (reading 18, writing 17, listening 17, speaking 20), PTE Academic 60 overall with 59 in each sub-skill, or Cambridge CAE 169 overall with a minimum of 162 in each sub-skill. Nationals of certain English-speaking countries (including the USA, Australia, Canada, Ireland, and others) are automatically exempt from the requirement.",
        "For most postgraduate courses, students need IELTS Academic 6.5 overall with no sub-skill below 6.0. Equivalent scores accepted include TOEFL iBT 88 overall, PTE Academic 62 overall with 60 in each sub-skill, or Cambridge CAE 176 overall. Some advanced postgraduate courses require IELTS 7.0 overall with no sub-skill below 6.0. All English language tests must be taken within two years of the course start date.",
        "The University of Stirling offers pre-sessional English language courses through its International Study Centre for students who do not yet meet the English language entry requirements. Options for September 2026 entry include: a 12-week online course (1 June – 21 August 2026) for £5,000; an 8-week online course (29 June – 21 August 2026) for £3,500; a 10-week on-campus course (15 June – 21 August 2026) for £5,000; and a 6-week on-campus course (13 July – 21 August 2026) for £3,200. The courses target students with current IELTS levels between 5.0 and 6.5 and include 20–25 hours of study per week.",
        "The International Undergraduate Scholarship is worth £2,500 per year (£10,000 over a standard four-year degree). It is automatically awarded to all eligible international (including EU) students who receive a conditional or unconditional offer for a full-time undergraduate course. Students are identified automatically during the admissions process — no separate application is needed. It cannot be combined with other University of Stirling scholarships (except the Sports Scholarship).",
        "The Vice Chancellor's Postgraduate International Scholarship provides a £7,000 tuition fee waiver for international postgraduate students studying a full-time Masters degree on campus. 100 awards are available for September 2026 and January 2027 entry. Applicants must be self-funded, new students, and hold a conditional or unconditional offer. A £1,000 deposit is required to secure the scholarship. Applications are assessed within approximately four weeks. Contact: international@stir.ac.uk.",
        "Yes. The EU Undergraduate Scholarship offers EU students a £5,000 fee discount per year of study, with an unlimited number of awards available. There is also the GEMS International Undergraduate Scholarship worth £8,000 (£2,000 per year over four years) available to all international students including those from the EU.",
        "The Stirling Success Scholarship is worth £5,000 and is available to undergraduate students from England, Wales, Northern Ireland, and the Republic of Ireland. It is designed to help with the cost of studying at Stirling for students from these regions.",
        "Yes. The University of Stirling offers an International Sports Scholarship Programme worth up to £5,000 per year for high-performance athletes of all nationalities. Separate Sports Scholarships are also available for students from England, Wales, Northern Ireland, the Republic of Ireland, the EU, and internationally, with up to 18 awards available. Sports Scholarships can be combined with the International Undergraduate Scholarship.",
        "For UK/home students, the PhD (and MPhil) tuition fee in 2025/26 is £5,006 per year full-time, or £2,503 per year part-time. A registration-only fee of £500 applies in the final year.",
        "For international students, PhD fees at the University of Stirling in 2025/26 vary by subject area. Institute of Aquaculture students pay £27,400 full-time (£13,700 part-time); Biological and Environmental Sciences and Computing Science students pay £24,100 full-time (£12,050 part-time); all other subjects are £19,500 full-time (£9,750 part-time). Fees for 2026/27 increase to £30,100, £26,500, and £21,500 respectively for full-time students.",
        "The University of Stirling offers over 2,800 rooms across its on-campus and off-campus residences. More than 2,000 of those rooms are located directly on the 330-acre campus.",
        "University of Stirling accommodation rent includes heating, electricity, contents insurance, Wi-Fi, bedding and bed linen, and housekeeping assistance. A 24/7 security team and emergency support are also provided. All accommodation is self-catered.",
        "The most affordable on-campus undergraduate accommodation is Polwarth House at £109.19 per week (36-week contract). Other budget options include Pendreich Way at £112.65 per week (49-week, postgraduate), Fraser of Allander House from £121.62 per week (no basin), and Spittal Hill at £112.65 per week (36-week, returning undergraduates).",
        "Yes. The University of Stirling guarantees an offer of university-managed accommodation to all new first-year full-time students commencing in September, provided they meet the eligibility criteria and submit their application by the advised deadline (2025/26 accommodation allocation policy).",
        "Students apply for accommodation online through the university's accommodation portal after accepting an offer to study at Stirling. Login details are sent following offer acceptance. Students can choose to pay rent in full or in instalments. Postgraduate students are required to pay a £300 rent pre-payment to confirm their place. The accommodation team can be contacted at accommodation@stir.ac.uk or +44 (0)1786 467060, Monday to Friday 09:00–17:00.",
        "A student sport and fitness membership at the University of Stirling costs £21.75 per month on a direct debit, or £234.90 for a full 12-month upfront payment. Membership includes unlimited gym access, swimming, fitness classes, and recreational sport sessions.",
        "The University of Stirling's sport facilities include a gym with 100+ Technogym stations across two levels (a fitness suite and a dedicated strength and conditioning area with Eleiko bars and BLK BOX racks), a swimming pool convertible between 25m and 50m configurations, six indoor tennis courts, multiple sports halls, and purpose-built fitness studios. The university is branded as 'Scotland's University for Sporting Excellence'. Students can also join Sports Union clubs, Social Sport Leagues, and the Just Play Sport programme.",
        "The University of Stirling is ranked 1st in the UK and 2nd in the world for sport facilities (ISB 2024). The campus environment as a whole is ranked 1st in the UK and top 10 in the world (ISB 2024). The university has also received 5 QS Stars across teaching, employability, global engagement, research, facilities, and environmental impact (QS Stars University Ratings 2024).",
        "The University of Stirling has over 120 clubs and societies, ranging from athletics to anime, volleyball to video games. Every registered student is automatically a member of the Students' Union, which oversees all clubs and societies. Students can also start a new society if they cannot find one that matches their interests.",
        "The University of Stirling Students' Union is a democratically elected body led by students, for students. It oversees 120+ clubs and societies, provides academic representation and support, runs on-campus social venues, operates a merchandise shop, and publishes an events calendar. Every registered student is automatically a member. The Union can be contacted at theunion@stir.ac.uk, +44 (0)1786 467166, or via stirlingstudentsunion.com.",
        "The University of Stirling library holds more than 500,000 books and provides extensive research and study spaces. The library is described as state-of-the-art with dedicated areas for both individual and group study.",
        "The University of Stirling offers a wide range of student support through its Student Services Hub (located in Campus Central). Services include mental health and wellbeing support, disability and accessibility services, money and financial advice, careers guidance, academic support via Student Learning Services, chaplaincy, LGBTQ+ support, visa and immigration advice, and support for care-experienced and estranged students. The Hub can be contacted by live chat (Mon–Fri 10:00–12:00 and 14:00–16:00), phone at 01786 466022 (Mon–Fri 14:00–16:00), email at ask@stir.ac.uk, or in person Mon/Wed/Fri 11:00–14:00.",
        "Estimated monthly living costs for a University of Stirling student range from approximately £992 to £1,467. This includes accommodation of £400–£875 per month (university halls, self-catered, with utilities and Wi-Fi included), food and toiletries around £280, travel approximately £42 (monthly Stirling Uni Link bus pass), course materials around £40, and personal costs (gym, socialising, haircuts) around £180. Private renting in Stirling averages around £512.50/month for a shared property, plus approximately £85/month for gas and electricity.",
        "To be accepted onto a postgraduate taught degree at the University of Stirling, applicants normally need a minimum of a second-class Honours degree (2:2 or equivalent) from a UK university or an equivalent qualification from an overseas institution. Some courses require a 2:1 or above, relevant work experience, or subject-specific knowledge. International students who do not meet standard academic or English language entry requirements may be eligible for postgraduate pathway/progression programmes.",
        "To apply for a postgraduate course at the University of Stirling, all applicants must submit: undergraduate transcript and graduation certificate (or interim transcript if still studying), copies of academic qualifications and certificates, one professional or academic reference, and a supporting statement explaining motivation for the course. EU and international applicants must also provide a certified translated transcript (if applicable) and evidence of English language proficiency. International applicants requiring a student visa must additionally provide a copy of their valid passport and current visa (if already in the UK). Applications can be submitted year-round, up to one year before the course start date. Contact: postgraduate.admissions@stir.ac.uk or +44 (0)1786 466655.",
        "Yes. The Macrobert Arts Centre is located on the University of Stirling campus and serves as an independent cinema and theatre. The campus also features The Atrium, a central hub with restaurants, shops, and pop-up vendors. Other on-campus amenities include cafes, a supermarket, a health centre, the Students' Union, and the Sports Centre — all within the 330-acre campus grounds.",
    ]
}


def get_test_dataset():
    """Return the test dataset as a Hugging Face Dataset object."""
    return Dataset.from_dict(test_qa_pairs)


if __name__ == "__main__":
    dataset = get_test_dataset()
    print(f"Loaded test dataset with {len(dataset)} QA pairs")
    print("\nSample questions:")
    for i, q in enumerate(dataset["question"][:5], 1):
        print(f"{i}. {q}")
