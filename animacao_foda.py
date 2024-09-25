import flet as ft
import asyncio

def main(page:ft.Page):
    page.theme_mode=ft.ThemeMode.DARK
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.bgcolor=ft.colors.BLACK
    async def animate(e=None):
        while True:
            img.offset.y = -0.3
            img.scale.scale= 1.2
            img.opacity = 1
            img.update()
            await asyncio.sleep(4)
            
            img.offset.y = 0 
            img.scale.scale= 1
            img.opacity = 0
            img.update()
            await asyncio.sleep(4)
            
    img=ft.Image(
        src="https://www.pngall.com/wp-content/uploads/5/PS5-Controller-PNG-Image.png",
        offset=ft.Offset(x=0,y=0),
        scale=ft.Scale(scale=1),
        opacity= 0,
        animate_offset=ft.Animation(duration=4000,curve=ft.AnimationCurve.EASE),
        animate_scale=ft.Animation(duration=2000,curve=ft.AnimationCurve.EASE),
        animate_opacity=ft.Animation(duration=4000,curve=ft.AnimationCurve.EASE)
    )
    page.add(img)
    asyncio.run(animate())
if __name__=="__main__":
    ft.app(target=main)