import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7/+esm";

function test(){
    const payload = {
        action: d3.select("#action").property("value"),
        encoding: d3.select("#encoding").property("value"),
        inText: d3.select("#inText").property("value"),
        key: d3.select("#key").property("value"),
    }
    fetch(window.location.origin+"/articleAPI/DES?" + new URLSearchParams(payload))
    .then(res => res.json())
    .then(data => {
        console.log(data);
        tableFill(data);
        // console.log(data);
        // const outEl = d3.select("#output")
        // for (const key in data) {
        //     if (Array.isArray(data[key])) {
        //         outEl.append("p").text(`${key}:`)
        //         for (const i in data[key]) {
        //             outEl.append("p").html(`&#8195; ${data[key][i]}`)
        //         }
        //     } else {
        //         outEl.append("p").text(`${key}: ${data[key]}`)
        //     }
        // }
    });
}

function tableFill(data) {
    const mapping = [
        ["x", data.x],
        ["k", data.k],
        ["IP", data.IP],
        ["PC1", data.PC1],
        ["L16", data.R[16]],
        ["R16", data.L[16]],
        ["fin", data.y],
        
    ]
    for (let i = 0; i < 16; i++) {
        mapping.push([`L${i}`, data.L[i]]);
        mapping.push([`R${i}`, data.R[i]]);
        mapping.push([`C${i}`, data.C[i]]);
        mapping.push([`D${i}`, data.D[i]]);
        mapping.push([`LSC${i+1}`, data.C[i+1]]);
        mapping.push([`LSD${i+1}`, data.D[i+1]]);
        mapping.push([`E${i+1}`, data.E[i]]);
        mapping.push([`PC2${i+1}`, data.ki[i]]);
        mapping.push([`EXor${i+1}`, data.EXor[i]]);
        mapping.push([`P${i+1}`, data.F[i]]);
        for (let j = 0; j < 8; j++) {
            mapping.push([`s${i+1}${j+1}`, data.S[j][i]])
        }
    }
    
    for (let i = 0; i < mapping.length; i++) {
        d3.select(`#tab_${mapping[i][0]}`).text(mapping[i][1])    
    }
    
}
    
    

window.test = test;



