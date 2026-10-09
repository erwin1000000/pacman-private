from pydantic import BaseModel, Field, field_validator, ValidationError


class Level(BaseModel):
    width: int = Field(gt=0)
    height: int = Field(gt=0)


class Data(BaseModel):
    highscore_filename: str = "highscores.json"
    lives: int = Field(default=3, gt=0)
    pacgum: int = Field(default=42, gt=0)
    points_per_pacgum: int = Field(default=10, ge=0)
    points_per_super_pacgum: int = Field(default=0, ge=0)
    points_per_ghost: int = Field(default=0, ge=0)
    seed: int = Field(default=42, gt=0)
    level_max_time: int = Field(default=90, ge=0)
    levels: list[Level] = Field(default=[
            Level(**{
                "width": 28,
                "height": 31
            }),
            Level(**{
                "width": 28,
                "height": 31
            }),
            Level(**{
                "width": 32,
                "height": 35
            })
        ],
        min_length=1)