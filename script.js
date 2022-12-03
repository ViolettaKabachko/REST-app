// async function getData(url) {
//     let response = await fetch(url);
//     let content = await response.json();
//     console.log(content)
//     for (key in content) {
//         console.log(key, typeof(key))
//         console.log(content[key])
//     }    
//     return content
    
    
    
// }




addEventListener('DOMContentLoaded', () => {

    const sendData = async (url, data) => {       
        const response = await fetch(url, {
            method: 'POST',
            body: data
        })
        return await response.json();

    }

    const getData = async (url) => {

        let response = await fetch(url);
        let content = await response.json();
        console.log(content)   
        return content

    }
    
    const b_1 = document.querySelector(".btn");
    
    b_1.addEventListener('click', async () => {

        const selected = document.querySelector(".request").value;
        console.log(selected);        
        await sendData('http://127.0.0.1:5000', selected);
        const info = await getData("http://127.0.0.1:5000");
        const p = document.createElement('p');
        const form = document.querySelector('form')
        p.textContent = info['res'];
        p.className = 'info'
        form.appendChild(p);
        
    })
})





















// addEventListener('DOMContentLoaded', (event) => {

//     async function loadSmth() {
//         let xhr = new XMLHttpRequest()
//         xhr.open("GET", "http://127.0.0.1:5000", false)
//         xhr.send()
//         xhr.onload = () => {
//             if (xhr.status != 200) { 
//                 alert(`Ошибка ${xhr.status}: ${xhr.statusText}`)
//               } else { 
//                 const content = xhr.response
//                 alert(content)
//                 return content
//               }
//         }
//     }

//     document.querySelector(".btn").addEventListener("click", function () {
//         const formKey = document.querySelector(".request").value
//         const value = loadSmth()
//         console.log(value)
        
//         const content = value[formKey]
//         const el = document.createElement("p");
//         const body = document.body;
//         el.textContent = content
//         body.appendChild(el);
    
//     })

// });