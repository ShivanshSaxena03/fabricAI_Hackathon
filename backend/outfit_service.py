from openrouter_service import ask_ai
from image_service import generate_image


def generate_outfit(fabric, color, occasion, gender, body_type, season, style, fit, climate, culture):

    text_prompt = f"""
    You are a world-class fashion stylist and designer.

    Generate 3 complete professional outfit recommendations using the following user profile:

    Fabric: {fabric}
    Primary Color: {color}
    Occasion: {occasion}
    Gender: {gender}
    Body Type: {body_type}
    Season: {season}
    Style Preference: {style}
    Fit Preference: {fit}
    Climate: {climate}
    Cultural Preference: {culture}

    Requirements:

    For each outfit, provide:

    1. Outfit Name / Title
    2. Full outfit description (top, bottom, outerwear if applicable)
    3. Fabric usage and why it is suitable
    4. Color combination and harmony explanation
    5. Fit and silhouette explanation based on body type
    6. Styling details (layering, tuck, roll, drape, etc.)
    7. Accessories recommendation (shoes, watch, belt, etc.)
    8. Why this outfit is ideal for the occasion, season, and climate
    9. Professional stylist tip

    Output Format:

    OUTFIT 1:
    Name:
    Description:
    Fabric Logic:
    Color Logic:
    Fit Logic:
    Styling:
    Accessories:
    Occasion Suitability:
    Stylist Tip:

    OUTFIT 2:
    ...

    OUTFIT 3:
    ...

    Ensure recommendations are modern, realistic, and wearable.
    Use professional fashion terminology.
    Avoid vague or generic suggestions.
    """

    text_response = ask_ai(text_prompt)

    image_prompt = f"""
Ultra-realistic professional fashion photography of a {gender} model with {body_type} body type,

wearing a {color} {fabric} outfit designed for {occasion},

style: {style},
fit: {fit},
season: {season},
climate suitability: {climate},
cultural style: {culture},

full body shot, standing pose,
luxury fashion magazine editorial,
studio lighting, soft shadows,
high detail fabric texture,
realistic fabric drape and folds,
8k resolution, sharp focus,

fashion week quality,
Vogue magazine style,
clean background,
professional photography,
cinematic lighting,
premium designer outfit
"""
    prompt1 = f"""
Create a professional fashion designer sketch.

Design Details:
- Color: {color}
- Occasion: {occasion}
- Fabric: {fabric}

Instructions:
- Full-body front-facing fashion illustration.
- Clean black ink outline drawing.
- Minimalistic technical sketch style (fashion croquis).
- White background only (no scenery, no props).
- Emphasize garment silhouette, seams, cuts, and layering.
- Clearly illustrate fabric behavior based on {fabric} 
  (drape, stiffness, flow, texture, thickness).
- Add light hatching or subtle line shading to indicate fabric texture.
- Keep it elegant, structured, and runway-inspired.
- No text, no watermark, no color fill (outline sketch only).
"""
    image_url = generate_image(prompt1)

    return {

        "outfit_recommendations": text_response,

        "image_url": image_url
    }