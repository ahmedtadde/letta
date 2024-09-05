from pydantic import BaseModel, Field


class MemGPTUsageStatistics(BaseModel):
    completion_tokens: int = Field(0, description="The number of tokens generated by the agent.")
    prompt_tokens: int = Field(0, description="The number of tokens in the prompt.")
    total_tokens: int = Field(0, description="The total number of tokens processed by the agent.")
    step_count: int = Field(0, description="The number of steps taken by the agent.")