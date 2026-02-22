import replicate
import os

client = replicate.Client(
    api_token= os.getenv("REPLICATE_API_TOKEN")
)

def generate_image(prompt):

    try:

        output = client.run(
            "black-forest-labs/flux-schnell",
            input={
                "prompt": f"Professional fashion photography, {prompt}, ultra realistic, studio lighting, fashion magazine",
                "aspect_ratio": "1:1",
                "output_format": "png"
            }
        )

        print("Output:", output)  # DEBUG
        return str(output)

    except Exception as e:

        print("Replicate error:", e)

        return "https://plus.unsplash.com/premium_photo-1762875982545-30fbe20a45b6?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"