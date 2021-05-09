import axios from "axios";
import {REPORT_LOCALHOST, CONFIG} from "./constants";

export default {
    createDocReport(data) {
        return axios.post(`${REPORT_LOCALHOST}/doc_report`, data, CONFIG)
    },

    createPatientReport(data) {
        return axios.post(`${REPORT_LOCALHOST}/patient_report`, data, CONFIG)
    },

    download(filename) {
        let config = {
            url: `${REPORT_LOCALHOST}/download/${filename}`,
            responseType: 'arraybuffer',
            method: 'GET',
        };

        return axios({
            ...config,
            transformResponse: function (data, headers) {
                let header = headers['content-disposition'];
                if (header) {
                    let filename = header.split(';')[1].trim().split('=')[1].replace(/"/g, '').replace("UTF-8''", "");
                    return {
                        data: data,
                        filename: decodeURIComponent(filename)
                    }
                } else {
                    if (data && data.byteLength > 0) {
                        return data;
                    } else {
                        return null;
                    }
                }
            }
        }).then(response => {
            if (response.data) {
                let type = null;
                if (filename.endsWith('.docx')) {
                    type = {type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'};
                } else if (filename.endsWith('.doc')) {
                    type = {type: 'application/msword'};
                }
                let url = URL.createObjectURL(new Blob([response.data], type));
                let a = document.createElement('a');
                a.href = url;
                a.download = decodeURIComponent(filename);
                a.target = '_blank';
                let evt = new MouseEvent("click", {
                    view: window,
                    bubbles: true,
                    cancelable: true
                });
                a.dispatchEvent(evt);
            }
        });
    },

    removeFromFolder(filename) {
        return axios.get(`${REPORT_LOCALHOST}/remove/${filename}`)
    }
}