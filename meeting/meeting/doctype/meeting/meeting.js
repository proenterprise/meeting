// Copyright (c) 2019, Adam Dawoodjee and contributors
// For license information, please see license.txt

frappe.ui.form.on('Meeting', {
    // refresh: function(frm) {

    // }, 

    send_emails: function(frm) {
        //if(frm.doc.status === "Planned"){
            frappe.call({
                method: "meeting.api.send_invitation_emails",
                args: {
                    meeting: frm.doc.name
                }
            });
        //}
    }
});

frappe.ui.form.on('Meeting Attendee', {
    attendee: function(frm, cdt, cdn) {
        var attendee = frappe.model.get_doc(cdt, cdn);
        if(attendee.attendee){
            frappe.call({
                method: "meeting.meeting.doctype.meeting.meeting.get_full_name",
                args: {
                    attendee: attendee.attendee
                },
                callback: function(r) {
                    frappe.model.set_value(cdt, cdn, "full_name", r.message)
                }
            });
        }
        else {
            frappe.model.set_value(cdt, cdn, "full_name", null);
        }
    }
});