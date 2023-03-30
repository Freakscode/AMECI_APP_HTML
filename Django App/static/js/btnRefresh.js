const devCaract = async (data) => {
    console.log("Getting device data...");
    document.getElementById('NameDev').innerText = data.name;
    document.getElementById('IPtxt').innerText = data.ip;
    document.getElementById('Port').innerText = data.port;
    document.getElementById('Status').innerText = data.status;
};

const cargaInicial = async() =>{
    console.log("Loading initial data...");
    const response = await fetch("http://127.0.0.1:8000/biomconf/device_connection_data/");
    const data = await response.json();
    if(data.message === 'Conexión exitosa'){
        await devCaract(data);
    } else {
        // set the text of the <p> elements to "no info found"
        await devCaract({'name': '--', 'ip': '--', 'port': '--', 'status': '--'});
    }
};

const refreshBtn = document.getElementById('refresh-btn');

refreshBtn.addEventListener('click', async () => {
    try {
        const response = await fetch("http://127.0.0.1:8000/biomconf/device_connection_data/");
        const data = await response.json();
        if(data.message === 'Conexión exitosa'){
            await devCaract(data);
        } else {
            // set the text of the <p> elements to "no info found"
            await devCaract({'name': '--', 'ip': '--', 'port': '--', 'status': '--'});
        }
    } catch (error) {
        console.log(error);
    }
});

window.addEventListener('load', async()=>{
    await cargaInicial();
});