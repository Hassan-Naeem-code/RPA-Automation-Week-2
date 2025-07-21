# 📊 Invoice Processing Automation - System Flowchart

## 🎯 Process Overview Flowchart

```mermaid
flowchart TD
    A[🚀 Start Invoice Automation] --> B{📂 Check Input File}
    B -->|File Exists| C[📋 Load Invoice Data]
    B -->|File Missing| Z1[❌ Error: File Not Found]
    
    C --> D{🔍 Validate Data Structure}
    D -->|Valid| E[🧹 Data Cleaning & Processing]
    D -->|Invalid| Z2[❌ Error: Invalid Data Format]
    
    E --> F[📊 Data Validation & Enrichment]
    F --> G{✅ Data Quality Check}
    G -->|Pass| H[💾 Save Processed Data]
    G -->|Fail| Z3[❌ Error: Data Quality Issues]
    
    H --> I[📈 Generate Executive Summary]
    I --> J[👥 Generate Client Analysis]
    J --> K[⏰ Generate Aging Analysis]
    K --> L[📊 Generate Status Breakdown]
    L --> M[📋 Compile Final Report]
    
    M --> N{📧 Email Enabled?}
    N -->|Yes| O[📨 Prepare Email]
    N -->|No| P[✅ Process Complete]
    
    O --> Q{🔐 SMTP Config Valid?}
    Q -->|Yes| R[📤 Send Email with Report]
    Q -->|No| S[⚠️ Warning: Email Skipped]
    
    R --> T{📬 Email Sent?}
    T -->|Success| U[✅ Email Delivered]
    T -->|Failed| V[❌ Email Failed]
    
    U --> P
    S --> P
    V --> P
    
    Z1 --> W[📝 Log Error]
    Z2 --> W
    Z3 --> W
    W --> X[🔄 Cleanup & Exit]
    
    P --> Y[📊 Display Summary]
    Y --> END[🎉 Process Finished]
    X --> END
    
    style A fill:#e1f5fe
    style P fill:#c8e6c9
    style END fill:#c8e6c9
    style Z1 fill:#ffcdd2
    style Z2 fill:#ffcdd2
    style Z3 fill:#ffcdd2
    style W fill:#fff3e0
    style U fill:#c8e6c9
    style V fill:#ffcdd2
```

## 🔄 Detailed Process Flow

### 1. 📥 Data Ingestion Phase
```mermaid
flowchart LR
    A[Excel File Input] --> B[File Validation]
    B --> C[Column Structure Check]
    C --> D[Data Type Validation]
    D --> E[Record Count Verification]
    E --> F[Data Loaded Successfully]
    
    style A fill:#e3f2fd
    style F fill:#c8e6c9
```

### 2. 🧹 Data Processing Phase
```mermaid
flowchart TD
    A[Raw Invoice Data] --> B[Remove Duplicates]
    B --> C[Validate Invoice IDs]
    C --> D[Clean Client Names]
    D --> E[Validate Amounts]
    E --> F[Standardize Status Values]
    F --> G[Format Dates]
    G --> H[Calculate Derived Fields]
    H --> I[Quality Score Assignment]
    I --> J[Processed Data Ready]
    
    style A fill:#fff3e0
    style J fill:#c8e6c9
```

### 3. 📊 Report Generation Phase
```mermaid
flowchart TD
    A[Processed Data] --> B[Create Excel Workbook]
    B --> C[Executive Summary Sheet]
    B --> D[Client Analysis Sheet]
    B --> E[Aging Analysis Sheet]
    B --> F[Status Breakdown Sheet]
    B --> G[Quality Metrics Sheet]
    B --> H[Time Series Sheet]
    B --> I[Raw Data Sheet]
    
    C --> J[Apply Formatting]
    D --> J
    E --> J
    F --> J
    G --> J
    H --> J
    I --> J
    
    J --> K[Add Charts & Graphs]
    K --> L[Save Report File]
    L --> M[Report Generated Successfully]
    
    style A fill:#e8f5e8
    style M fill:#c8e6c9
```

### 4. 📧 Email Distribution Phase
```mermaid
flowchart TD
    A[Report Generated] --> B{Email Configuration}
    B -->|Configured| C[Create Email Message]
    B -->|Not Configured| D[Skip Email Step]
    
    C --> E[Attach Report File]
    E --> F[Format HTML Email]
    F --> G[Connect to SMTP Server]
    G --> H{Connection Success?}
    
    H -->|Yes| I[Send Email]
    H -->|No| J[Log Connection Error]
    
    I --> K{Email Sent?}
    K -->|Success| L[✅ Email Delivered]
    K -->|Failed| M[❌ Send Failed]
    
    D --> N[Process Complete]
    L --> N
    M --> N
    J --> N
    
    style L fill:#c8e6c9
    style M fill:#ffcdd2
    style N fill:#e1f5fe
```

## 🏗️ System Architecture Flow

```mermaid
flowchart TB
    subgraph "🎮 Main Controller"
        A[main.py]
    end
    
    subgraph "📊 Data Processing Layer"
        B[process_data.py]
        B1[Data Validation]
        B2[Data Cleaning]
        B3[Data Enrichment]
    end
    
    subgraph "📈 Report Generation Layer"
        C[generate_report.py]
        C1[Executive Summary]
        C2[Client Analysis]
        C3[Aging Analysis]
        C4[Status Reports]
    end
    
    subgraph "📧 Communication Layer"
        D[send_email.py]
        D1[Email Formatting]
        D2[SMTP Connection]
        D3[Attachment Handling]
    end
    
    subgraph "💾 Data Storage"
        E[(Excel Files)]
        F[(Config Files)]
        G[(Log Files)]
    end
    
    A --> B
    B --> B1
    B1 --> B2
    B2 --> B3
    B3 --> C
    
    C --> C1
    C1 --> C2
    C2 --> C3
    C3 --> C4
    C4 --> D
    
    D --> D1
    D1 --> D2
    D2 --> D3
    
    B <--> E
    C <--> E
    A <--> F
    A --> G
    
    style A fill:#e1f5fe
    style E fill:#fff3e0
    style F fill:#f3e5f5
    style G fill:#e8f5e8
```

## 📋 Error Handling Flow

```mermaid
flowchart TD
    A[Process Step] --> B{Error Occurred?}
    B -->|No| C[Continue to Next Step]
    B -->|Yes| D[Capture Error Details]
    
    D --> E[Log Error Message]
    E --> F[Determine Error Type]
    
    F -->|Fatal| G[Stop Process]
    F -->|Warning| H[Continue with Warning]
    F -->|Recoverable| I[Attempt Recovery]
    
    I --> J{Recovery Success?}
    J -->|Yes| K[Log Recovery Success]
    J -->|No| L[Log Recovery Failed]
    
    K --> C
    L --> G
    H --> C
    G --> M[Cleanup Resources]
    M --> N[Exit with Error Code]
    
    C --> O[Process Complete]
    
    style G fill:#ffcdd2
    style N fill:#ffcdd2
    style O fill:#c8e6c9
```

## 🔍 Data Quality Validation Flow

```mermaid
flowchart TD
    A[Input Data] --> B[Check Required Columns]
    B --> C{All Columns Present?}
    C -->|No| D[❌ Missing Columns Error]
    C -->|Yes| E[Validate Data Types]
    
    E --> F{Correct Types?}
    F -->|No| G[❌ Type Validation Error]
    F -->|Yes| H[Check Value Ranges]
    
    H --> I{Values in Range?}
    I -->|No| J[❌ Range Validation Error]
    I -->|Yes| K[Check Business Rules]
    
    K --> L{Rules Satisfied?}
    L -->|No| M[❌ Business Rule Error]
    L -->|Yes| N[✅ Data Valid]
    
    D --> O[Generate Error Report]
    G --> O
    J --> O
    M --> O
    O --> P[Stop Processing]
    
    N --> Q[Proceed with Processing]
    
    style N fill:#c8e6c9
    style P fill:#ffcdd2
    style Q fill:#e1f5fe
```

## 📈 Performance Monitoring Flow

```mermaid
flowchart LR
    A[Start Timer] --> B[Execute Process Step]
    B --> C[End Timer]
    C --> D[Calculate Duration]
    D --> E[Log Performance Metric]
    E --> F[Update Running Statistics]
    F --> G{Performance Threshold?}
    G -->|Above| H[⚠️ Performance Warning]
    G -->|Within| I[✅ Performance OK]
    H --> J[Log Warning]
    I --> K[Continue Processing]
    J --> K
    
    style H fill:#fff3e0
    style I fill:#c8e6c9
```

---

## 📝 Flow Legend

| Symbol | Meaning |
|--------|---------|
| 🚀 | Start/Initialization |
| 📂 | File Operations |
| 🔍 | Validation/Checking |
| 🧹 | Data Processing |
| 📊 | Analysis/Calculation |
| 📈 | Report Generation |
| 📧 | Email Operations |
| ✅ | Success State |
| ❌ | Error State |
| ⚠️ | Warning State |
| 🎉 | Completion |

---

*Generated for Concordia University RPA Course - Hassan Naeem*
