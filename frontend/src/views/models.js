export class User {
    id;
    login;
    password;
    access_level;
}

export class Patient {
    id
    user_id
    policy_num
    first_name
    last_name
    middle_name
    gender
    age
    weight
    height
    has_nuo
    prob_log_reg
    prob_rnd_forest
    prob_log_svm
}

export class Doctor {
    id
    user_id
    full_name
    cabinet
    telephone
}

export class EKG {
    id;
    patient_id
    registry_date
    sdnn
    skewness
    amo
    swai
    mo
    drr
    rrnn
    pnn50
    si
    sati
    rmi
    kurtosis
    cv
    rmssd
    nn50
    lf
    lfhf
    hfp
    ulf
    tp
    vlf
    vlfp
    lfp
    br
    ulfp
    ic
    hf
    tpfull
    p_left_slopes
    p_right_slopes
    q_left_slopes
    q_right_slopes
    t_left_slopes
    t_right_slopes
    qt
    st
    p
    pq
    qrs
    pulse
}