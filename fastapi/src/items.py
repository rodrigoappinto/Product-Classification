from pydantic import BaseModel, Field


class ProductClassificationItem(BaseModel):
    title: str = Field(
        description="Product title.",
        example="Happy Forever Cross Stitch, Chinese style animal dragon, Tsing lung",
    )
    description: list[str] = Field(
        description="Product description.",
        example=[
            "Happy forever cross-stitch kits are 11ct stamped, high-end and 100% accurate pre-printed cross stitch kits,You don't have to read the chart because each printed graph has symbols and color blocks. It's much easier more fun and faster to finish. Full stitch usually use 3 strands of thread, Back stitch use 2 strands of thread, and the threads all have the line numbers of international standard, if you ran out of the thread, you can almost find it in Walmart, even not, please contact us anytime. Kit includes: Fabric, Enough thread, Needles, Colorful chart standby, Instruction in English & Chinese."
        ],
    )
    brand: str = Field(description="Happy forever", example="Speed Dealer Customs")
    features: list[str] = Field(
        description="Product features.",
        example=["Happy forever cross-stitch kits are 11ct stamped, high-end and 100% accurate pre-printed cross stitch kits,You don't have to read the chart because each printed graph has symbols and color blocks. It's much easier more fun and faster to finish. Full stitch usually use 3 strands of thread, Back stitch use 2 strands of thread, and the threads all have the line numbers of international standard, if you ran out of the thread, you can almost find it in Walmart, even not, please contact us anytime. Kit includes: Fabric, Enough thread, Needles, Colorful chart standby, Instruction in English & Chinese.", "Finished Size:35-inches by 47-inches"],
    )
