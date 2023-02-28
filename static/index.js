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
        ["L0", data.L[0]],
        ["R0", data.R[0]],
        ["C0", data.C[0]],
        ["D0", data.D[0]],
        ["LSC1", data.C[1]],
        ["LSD1", data.D[1]],
        ["E1", data.E[0]],
        ["PC21", data.ki[0]],
        ["EXor1", data.EXor[0]],
        ["P1", data.F[0]]
    ]
    for (let i = 0; i < 8; i++) {
        mapping.push([`s1${i+1}`, data.S[1][i]])
    }
    for (let i = 0; i < mapping.length; i++) {
        d3.select(`#tab_${mapping[i][0]}`).text(mapping[i][1])    
    }
    
}
    
    

window.test = test;



