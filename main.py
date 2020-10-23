import asyncio

import iterm2



async def start_frontend(session: iterm2.Session):
    await session.async_send_text('npm start \n')

async def start_backend(session: iterm2.Session):
    await session.async_send_text('source  env/bin/activate \n')
    await session.async_send_text('docker-compose up -d \n')
    await session.async_send_text('./dev.sh \n')

async def start_socket(session: iterm2.Session):
    await session.async_send_text('npm run dev \n')

async def start_reporter(session: iterm2.Session):
    await session.async_send_text('npm run dev \n')





async def main(connection):
    app = await iterm2.async_get_app(connection)
    window = app.current_window
    if window is not None:
        tab = await window.async_create_tab()
        pane1 = tab.current_session
        pane2 = await pane1.async_split_pane(vertical=True)
        pane3 = await pane2.async_split_pane(vertical=False)

        await pane1.async_activate()
        session2 = tab.current_session
        pane4 = await session2.async_split_pane(vertical=False)

        await pane1.async_send_text('cd /Users/markwilkins/projects/enrichment-tracking-front-end-v2 \n')
        await pane2.async_send_text('cd /Users/markwilkins/projects/enrichment-tracking-socket-server \n')
        await pane3.async_send_text('cd /Users/markwilkins/projects/python-rest \n')
        await pane4.async_send_text('cd /Users/markwilkins/projects/ths-data-reporter \n')

        p1 = start_frontend(pane1)
        p2 = start_backend(pane3)
        p3 = start_socket(pane2)
        p4 = start_reporter(pane4)

        await asyncio.wait([p1, p2, p3, p4], return_when=asyncio.ALL_COMPLETED)
    else:
        print("No current window")


if __name__ == '__main__':
    iterm2.run_until_complete(main)

