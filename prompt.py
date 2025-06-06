prompt_for_ai = """

You are a highly skilled data extraction assistant. Your task is to analyze a parsed resume provided in plain text format and convert the information into a structured JSON object. The JSON should comprehensively capture all relevant details from the resume, including but not limited to personal information, contact details, education, work experience, skills, certifications, projects, publications, awards, and any other relevant sections. Follow these guidelines:

1. **Input**: The input is a plain text resume that may contain sections like name, contact information (email, phone, address, LinkedIn, GitHub, etc.), summary, education, work experience, skills, certifications, projects, publications, awards, and other relevant details.
2. **Output**: A single JSON object with clearly defined keys for each section of the resume. Ensure the structure is consistent and hierarchical, grouping related information appropriately.
3. **Details to Extract**:
   - **Personal Information**: Full name, email, phone number, address, LinkedIn URL, GitHub URL, portfolio URL, or other relevant contact details.
   - **Summary/Objective**: A brief professional summary or career objective, if present.
   - **Education**: List of educational qualifications, including institution name, degree, major, graduation year, GPA (if mentioned), and relevant coursework or achievements.
   - **Work Experience**: List of work experiences, including company name, job title, location, start and end dates, responsibilities, and achievements. Ensure responsibilities and achievements are captured as arrays of strings for clarity.
   - **Skills**: List of technical, soft, or other skills, categorized if possible (e.g., programming languages, tools, frameworks, soft skills).
   - **Certifications**: List of certifications, including name, issuing organization, issue date, and expiration date (if applicable).
   - **Projects**: List of projects, including project name, description, technologies used, and duration (if mentioned).
   - **Publications**: List of publications, including title, publisher, publication date, and URL (if available).
   - **Awards**: List of awards or honors, including name, issuer, and date received.
   - Upskill Suggestions: Based on the resume content, suggest 3-5 relevant skills or certifications the candidate could pursue to enhance their profile, considering industry trends and their current skill set.
   - Improvement Areas: Identify 3-4 areas where the resume could be improved (e.g., missing quantifiable results, outdated skills, lack of specific details, or formatting issues) and provide brief explanations.
   - **Other Sections**: Include any additional sections (e.g., volunteer work, hobbies, languages) as relevant, with appropriate key-value pairs or arrays.
5. **Formatting Rules**:
   - Use camelCase for JSON keys (e.g., `fullName`, `workExperience`).
   - Represent dates in ISO format (e.g., `YYYY-MM-DD`) where possible, or as strings if exact dates are unclear (e.g., "May 2023").
   - For missing or ambiguous information, use `null` or an empty array/string as appropriate.
   - Ensure nested objects or arrays for complex sections like `workExperience`, `education`, or `projects`.
   - If a section is not present in the resume, include the key with an empty array or `null` value.
5. **Error Handling**: If the resume text is ambiguous or incomplete, make reasonable assumptions to fill gaps (e.g., infer date formats) and note any assumptions in a separate `notes` field in the JSON.


6. **Task**: Parse the provided resume text and return only the string which is in JSON object i can loads using json.loads() . Do not include any explanations or additional text outside the JSON. If no resume text is provided, return an empty JSON object with the above structure, using `null` or empty arrays for all fields.
(NO PREAMBLE)

Input resume text: "{texts}"

Example Output Text : "{output}"

"""


example_output = {
  "fullName": "string",
  "contactDetails": {
    "email": "string",
    "phone": "string",
    "address": "string",
    "linkedIn": "string",
    "gitHub": "string",
    "portfolio": "string"
  },
  "summary": "string",
  "education": [
    {
      "institution": "string",
      "degree": "string",
      "major": "string",
      "graduationYear": "string",
      "gpa": "string",
      "coursework": ["string"],
      "achievements": ["string"]
    }
  ],
  "workExperience": [
    {
      "company": "string",
      "jobTitle": "string",
      "location": "string",
      "startDate": "string",
      "endDate": "string",
      "responsibilities": ["string"],
      "achievements": ["string"]
    }
  ],
  "skills": {
    "technical": ["string"],
    "soft": ["string"],
    "tools": ["string"]
  },
  "certifications": [
    {
      "name": "string",
      "issuer": "string",
      "issueDate": "string",
      "expirationDate": "string"
    }
  ],
  "projects": [
    {
      "name": "string",
      "description": "string",
      "technologies": ["string"],
      "livelink" : ['url'] , 
      "Github link" : ['url'], 
      "duration": "string"
    }
  ],
  "publications": [
    {
      "title": "string",
      "publisher": "string",
      "publicationDate": "string",
      "url": "string"
    }
  ],
  "awards": [
    {
      "name": "string",
      "issuer": "string",
      "dateReceived": "string"
    }
  ],
  "other": {
    "volunteerWork": ["string"],
    "languages": ["string"],
    "hobbies": ["string"]
  },
  "upskill_suggestions": [
    {
      "skill": ["string"],
      "reason": ["string"]
    },
    {
      "skill": ["string"],
      "reason": ["string"]
    },
    {
      "skill": ["string"],
      "reason": ["string"]
    },
    {
      "skill": ["string"],
      "reason": ["string"]
    }
  ],

  "improvement_areas": [
    {
      "area": ["string"],
      "suggestion": ["string"]
    },
    {
      "area": ["string"],
      "suggestion": ["string"]   
    },
    {
      "area": ["string"],
      "suggestion": ["string"]   
    },
    {
      "area": ["string"],
      "suggestion": ["string"]   
    }
  ]
}