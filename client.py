import streamlit as st
import requests



def invoice_form(data):
    placeholder = st.empty()
    with placeholder.form("my_form"):
        name = st.text_input("Vendor Name",value=data['vendor'])
        invoice_no = st.text_input("Invoice No",value=data['number'])
        invoice_date = st.text_input("Invoice Date",value=data['date'])
        amount = st.text_input("Invoice Amount",value=data['amount'])

        submit=st.form_submit_button(on_click=msg)
        if submit:
            placeholder.empty()
            
        
def msg():
    st.success("Data sumbitted successfully")

def uploaded():
    st.session_state['submitted'] = True
        
def main():
    st.set_page_config(page_title="PDF Upload and Display")
    st.title("Vendor Invoice Uploader")
    st.sidebar.markdown('<span style="font-size:25px">About the System</span>',unsafe_allow_html=True)
    st.sidebar.markdown(
                         '<span style="font-size:20px">Upload the invoice pdf and the system will extract the    details for submission.</span>',unsafe_allow_html=True
                         )
    if 'submitted' not in st.session_state:
        st.session_state['submitted']= False
        st.session_state['data']= {}
   
    with st.form("my_form1",clear_on_submit=True):
        pdf_file = st.file_uploader("Upload the invoice PDF", type=["pdf"])

        submitted=st.form_submit_button(label="Upload and Generate",on_click=uploaded)

        if submitted:
    
            files = {"file":pdf_file.getvalue()}
            r = requests.post(url="http://127.0.0.1:8000/upload", files=files)
            st.session_state['data']= r.json()
            
            
    if st.session_state['submitted']:
        invoice_form(st.session_state['data'])
              

    
if __name__ == '__main__':
    main()