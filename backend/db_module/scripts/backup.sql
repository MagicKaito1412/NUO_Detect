--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.21
-- Dumped by pg_dump version 9.6.21

-- Started on 2021-03-26 03:09:36

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 1 (class 3079 OID 12387)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2166 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 190 (class 1259 OID 16661)
-- Name: doctors; Type: TABLE; Schema: public; Owner: u1
--

CREATE TABLE public.doctors (
    doctor_id bigint NOT NULL,
    user_id bigint NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(50) NOT NULL,
    middle_name character varying(50),
    cabinet real,
    telephone integer NOT NULL
);


ALTER TABLE public.doctors OWNER TO u1;

--
-- TOC entry 189 (class 1259 OID 16659)
-- Name: doctors_doctor_id_seq; Type: SEQUENCE; Schema: public; Owner: u1
--

CREATE SEQUENCE public.doctors_doctor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.doctors_doctor_id_seq OWNER TO u1;

--
-- TOC entry 2167 (class 0 OID 0)
-- Dependencies: 189
-- Name: doctors_doctor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: u1
--

ALTER SEQUENCE public.doctors_doctor_id_seq OWNED BY public.doctors.doctor_id;


--
-- TOC entry 192 (class 1259 OID 16676)
-- Name: ekgs; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ekgs (
    ekg_id bigint NOT NULL,
    patient_id bigint NOT NULL,
    registry_date timestamp without time zone NOT NULL,
    sdnn double precision,
    skewness double precision,
    amo double precision,
    swai double precision,
    mo double precision,
    drr double precision,
    rrnn double precision,
    pnn50 double precision,
    si double precision,
    sati double precision,
    rmi double precision,
    kurtosis double precision,
    cv double precision,
    rmssd double precision,
    nn50 double precision,
    lf double precision,
    lfhf double precision,
    hfp double precision,
    ulf double precision,
    tp double precision,
    vlf double precision,
    vlfp double precision,
    lfp double precision,
    br double precision,
    ulfp double precision,
    ic double precision,
    hf double precision,
    tpfull double precision,
    p_left_slopes double precision,
    p_right_slopes double precision,
    q_left_slopes double precision,
    q_right_slopes double precision,
    t_left_slopes double precision,
    t_right_slopes double precision,
    qt double precision,
    st double precision,
    p double precision,
    pq double precision,
    qrs double precision,
    pulse integer,
    prob_log_reg real,
    prob_rnd_forest real,
    prob_log_svm real,
    has_nuo integer
);


ALTER TABLE public.ekgs OWNER TO postgres;

--
-- TOC entry 191 (class 1259 OID 16674)
-- Name: ekgs_ekg_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ekgs_ekg_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ekgs_ekg_id_seq OWNER TO postgres;

--
-- TOC entry 2168 (class 0 OID 0)
-- Dependencies: 191
-- Name: ekgs_ekg_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ekgs_ekg_id_seq OWNED BY public.ekgs.ekg_id;


--
-- TOC entry 188 (class 1259 OID 16644)
-- Name: patients; Type: TABLE; Schema: public; Owner: u1
--

CREATE TABLE public.patients (
    patient_id bigint NOT NULL,
    user_id bigint NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(50) NOT NULL,
    middle_name character varying(50),
    gender integer NOT NULL,
    age integer NOT NULL,
    weight integer NOT NULL,
    height integer NOT NULL,
    policy_num character varying(16) NOT NULL,
    has_nuo integer,
    prob_log_reg real,
    prob_rnd_forest real,
    prob_log_svm real
);


ALTER TABLE public.patients OWNER TO u1;

--
-- TOC entry 187 (class 1259 OID 16642)
-- Name: patients_patient_id_seq; Type: SEQUENCE; Schema: public; Owner: u1
--

CREATE SEQUENCE public.patients_patient_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.patients_patient_id_seq OWNER TO u1;

--
-- TOC entry 2169 (class 0 OID 0)
-- Dependencies: 187
-- Name: patients_patient_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: u1
--

ALTER SEQUENCE public.patients_patient_id_seq OWNED BY public.patients.patient_id;


--
-- TOC entry 186 (class 1259 OID 16634)
-- Name: users; Type: TABLE; Schema: public; Owner: u1
--

CREATE TABLE public.users (
    user_id bigint NOT NULL,
    password character varying(60) NOT NULL,
    login character varying(30) NOT NULL,
    access_level integer NOT NULL
);


ALTER TABLE public.users OWNER TO u1;

--
-- TOC entry 185 (class 1259 OID 16632)
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: u1
--

CREATE SEQUENCE public.users_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO u1;

--
-- TOC entry 2170 (class 0 OID 0)
-- Dependencies: 185
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: u1
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- TOC entry 2021 (class 2604 OID 16664)
-- Name: doctors doctor_id; Type: DEFAULT; Schema: public; Owner: u1
--

ALTER TABLE ONLY public.doctors ALTER COLUMN doctor_id SET DEFAULT nextval('public.doctors_doctor_id_seq'::regclass);


--
-- TOC entry 2022 (class 2604 OID 16679)
-- Name: ekgs ekg_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ekgs ALTER COLUMN ekg_id SET DEFAULT nextval('public.ekgs_ekg_id_seq'::regclass);


--
-- TOC entry 2020 (class 2604 OID 16647)
-- Name: patients patient_id; Type: DEFAULT; Schema: public; Owner: u1
--

ALTER TABLE ONLY public.patients ALTER COLUMN patient_id SET DEFAULT nextval('public.patients_patient_id_seq'::regclass);


--
-- TOC entry 2019 (class 2604 OID 16637)
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: u1
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- TOC entry 2034 (class 2606 OID 16666)
-- Name: doctors doctors_pkey; Type: CONSTRAINT; Schema: public; Owner: u1
--

ALTER TABLE ONLY public.doctors
    ADD CONSTRAINT doctors_pkey PRIMARY KEY (doctor_id);


--
-- TOC entry 2036 (class 2606 OID 16668)
-- Name: doctors doctors_user_id_key; Type: CONSTRAINT; Schema: public; Owner: u1
--

ALTER TABLE ONLY public.doctors
    ADD CONSTRAINT doctors_user_id_key UNIQUE (user_id);


--
-- TOC entry 2038 (class 2606 OID 16681)
-- Name: ekgs ekgs_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ekgs
    ADD CONSTRAINT ekgs_pkey PRIMARY KEY (ekg_id);


--
-- TOC entry 2028 (class 2606 OID 16649)
-- Name: patients patients_pkey; Type: CONSTRAINT; Schema: public; Owner: u1
--

ALTER TABLE ONLY public.patients
    ADD CONSTRAINT patients_pkey PRIMARY KEY (patient_id);


--
-- TOC entry 2030 (class 2606 OID 16653)
-- Name: patients patients_policy_num_key; Type: CONSTRAINT; Schema: public; Owner: u1
--

ALTER TABLE ONLY public.patients
    ADD CONSTRAINT patients_policy_num_key UNIQUE (policy_num);


--
-- TOC entry 2032 (class 2606 OID 16651)
-- Name: patients patients_user_id_key; Type: CONSTRAINT; Schema: public; Owner: u1
--

ALTER TABLE ONLY public.patients
    ADD CONSTRAINT patients_user_id_key UNIQUE (user_id);


--
-- TOC entry 2024 (class 2606 OID 16641)
-- Name: users users_login_key; Type: CONSTRAINT; Schema: public; Owner: u1
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_login_key UNIQUE (login);


--
-- TOC entry 2026 (class 2606 OID 16639)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: u1
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- TOC entry 2040 (class 2606 OID 16669)
-- Name: doctors doctors_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: u1
--

ALTER TABLE ONLY public.doctors
    ADD CONSTRAINT doctors_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2041 (class 2606 OID 16682)
-- Name: ekgs ekgs_patient_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ekgs
    ADD CONSTRAINT ekgs_patient_id_fkey FOREIGN KEY (patient_id) REFERENCES public.patients(patient_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 2039 (class 2606 OID 16654)
-- Name: patients patients_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: u1
--

ALTER TABLE ONLY public.patients
    ADD CONSTRAINT patients_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id) ON UPDATE CASCADE ON DELETE CASCADE;


-- Completed on 2021-03-26 03:09:37

--
-- PostgreSQL database dump complete
--

