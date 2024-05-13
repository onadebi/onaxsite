// Reference: SweetAlert - https://unpkg.com/sweetalert/dist/sweetalert.min.js
const isDev = true;
const BASE_URL = isDev ? 'http://localhost:8000/' : 'https://onaxsys.com/';
window.onload =async ()=>{
    const allContactReasons = await fetchEnquiryPurpose();
    const purposeSelector = document.querySelector('#purpose');

    const fragment = document.createDocumentFragment();
    allContactReasons.forEach((obj) => {
        const option = document.createElement('option'); // Create <option> element
        option.value = obj.key;
        option.textContent = obj.value;
        fragment.appendChild(option); // Append <option> to fragment
    });
    purposeSelector.appendChild(fragment);
}

const form = document.getElementById('frmContact');
form.addEventListener('submit', async function(event) {
    event.preventDefault();

    // Display an alert to confirm submission
    // const confirmed = confirm('Are you sure you want to submit this form?');
    // if (confirmed) {
        const formData = {};
        const inputs = this.querySelectorAll('input, select, textarea');

        let display = false;
        inputs.forEach(input => {
            const name = input.getAttribute('name');
            formData[name] = input.value;
            if (name === 'purpose') {
                if (formData[name] === '') {
                    alert('Select a valid purpose of contact');
                    return;
                }
                display = true;
            }
        });
        if(display){
            const data = {'contactObj':formData};
            console.log(JSON.stringify(data),formData);
            fetch(`${BASE_URL}api/messages/submit-contact`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')  // Function to retrieve CSRF token from cookie
                },
                body: JSON.stringify(formData)
            }).then(async (resp)=> {
                const objResult = await resp.json();
                console.log(objResult);
                if(objResult.isSuccessful){
                    swal({
                        title: `${CapitalizeFirstLetter(objResult.message)} 🙂👍`,
                        text:'Your message has been submitted. I would get back to you ASAP!',
                        icon: 'success'
                    });                
                    inputs.forEach(i=>{ i.value = ''});
                }else{
                    swal({
                        title: `${CapitalizeFirstLetter(objResult.message)}`,
                        text:'Message could not be sent. Kindly retry!',
                        icon: 'error'
                    }); 
                }
            }).catch((err)=>{
                swal({
                    title: CapitalizeFirstLetter(err.message),
                    text:`Seems an error occured 😥. Kindly try again.`,
                    icon: 'error'
                });   
            }).finally();

        }
});

//#region HELPER Functions
const fetchEnquiryPurpose = async ()=>{
    let purposeData = [];
    const response = await fetch(`${BASE_URL}api/messages/contact-options`);
    if(response.ok){
        const allContactInfo = await response.json();
        purposeData.push(...allContactInfo);
    }else{
        alert('Unable to retrieve data from the server. Kindly refresh your browser.');
        console.log(JSON.stringify(response))
    }
    return purposeData;
}

function getCookie(name) {
    const cookieValue = document.cookie.split('; ')
        .find(cookie => cookie.startsWith(name + '='))
        .split('=')[1];
    return cookieValue;
}

function CapitalizeFirstLetter(str){
    const [firstletter, ...others] = str;
    return `${firstletter.toUpperCase()}${others.join('')}`;
}
//#endregion