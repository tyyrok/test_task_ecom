from datetime import date

from pydantic import TypeAdapter, EmailStr


email_adapter = TypeAdapter(EmailStr)
date_adapter = TypeAdapter(date)
