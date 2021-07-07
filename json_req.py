from pydantic import BaseModel

# CustomerID,CheckingStatus,LoanDuration,CreditHistory,LoanPurpose,LoanAmount,ExistingSavings,EmploymentDuration,InstallmentPercent,Sex,
# OthersOnLoan,CurrentResidenceDuration,OwnsProperty,Age,InstallmentPlans,Housing,ExistingCreditsCount,Job,Dependents,Telephone,ForeignWorker,Risk

class Input(BaseModel):
    CheckingStatus: str
    LoanDuration: int
    CreditHistory: str
    LoanPurpose: str
    LoanAmount: int
    ExistingSavings: str
    EmploymentDuration: str
    InstallmentPercent: int
    Sex: str
    OthersOnLoan: str
    CurrentResidenceDuration: int
    OwnsProperty: str
    Age: int
    InstallmentPlans: str
    Housing: str
    ExistingCreditsCount: int
    Job: str
    Dependents: int
    Telephone: str
    ForeignWorker: str
