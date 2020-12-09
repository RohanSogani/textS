import React, { Component } from 'react';
import { Progress } from 'reactstrap';
import { ToastContainer, toast } from 'react-toastify';
import axios from 'axios';
import 'react-toastify/dist/ReactToastify.css';

class Upload extends Component {
    constructor(props) {
        super(props);
        this.state = {
            selectedFile: null
        }
    }

    onChangeHandler = (event) => {
        let files = event.target.files;
        console.log(files[0]);
        this.setState({
            selectedFile: files[0],
            loaded: 0
        })
    }

    onClickHandler = () => {
        const data = new FormData();
        let name = String(this.state.selectedFile.name)
        name = name.split('.')
        data.append('title', name)
        data.append('content', name)
        data.append('pdf', this.state.selectedFile);
        axios.post("http://localhost:8000/api/upload/", data,  {
            onUploadProgress: ProgressEvent => {
                this.setState({
                    loaded: (ProgressEvent.loaded / ProgressEvent.total * 100),
                })
            }
        }).then(res => {
            toast.success('Upload success')
            document.getElementById("textarea1").value = res.data
        }).catch(err => {
            toast.error('Upload fail')
        })
    }

    render() {
        const style = {
            height:'500px',
            width:'700px',
            padding:'9px',
            boxSizing:'border-box',
            fontSize:'15px'};
        const v1 = {
            borderLeft: '2px solid green',
        }
        return (
            <div className="container" style={{"margin-left": 0}}>
                <div className="row">
                    <div className="col-md-6">
                        <form method="post" action="#" id="#">
                            <div className="form-group files">
                                <label>Upload Your File </label>
                                <input type="file" className="form-control" multiple="" onChange={this.onChangeHandler}/>
                            </div>
                            <div className="form-group">
                                <ToastContainer />
                                <Progress max="100" color="success" value={this.state.loaded} >{Math.round(this.state.loaded,2) }%</Progress>
                            </div>
                            <button type="button" className="btn btn-s btn-success btn-block" onClick={this.onClickHandler}>Upload</button>
                        </form>
                    </div>
                    <div className="col-md-6">
                        <form>
                            <div className="form-group">
                                <label>Summary</label>
                                <textarea id="textarea1" style={style}/>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        );
    }
}
export default Upload;