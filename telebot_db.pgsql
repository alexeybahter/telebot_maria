--
-- PostgreSQL database dump
--

-- Dumped from database version 10.1
-- Dumped by pg_dump version 10.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: music; Type: TABLE; Schema: public; Owner: alexey
--

CREATE TABLE music (
    id integer NOT NULL,
    file_id text NOT NULL,
    right_answer text NOT NULL,
    wrong_answer text NOT NULL
);


ALTER TABLE music OWNER TO alexey;

--
-- Name: musicTable; Type: TABLE; Schema: public; Owner: alexey
--

CREATE TABLE "musicTable" (
    id integer NOT NULL,
    file_id text NOT NULL,
    right_answer text NOT NULL,
    wrong_answer text NOT NULL
);


ALTER TABLE "musicTable" OWNER TO alexey;

--
-- Data for Name: music; Type: TABLE DATA; Schema: public; Owner: alexey
--

COPY music (id, file_id, right_answer, wrong_answer) FROM stdin;
1	key1	good	bad
2	key2	good2	bad2
3	key3	good3	bad3
4	keys4	good4	bad4
\.


--
-- Data for Name: musicTable; Type: TABLE DATA; Schema: public; Owner: alexey
--

COPY "musicTable" (id, file_id, right_answer, wrong_answer) FROM stdin;
\.


--
-- Name: musicTable musicTable_pkey; Type: CONSTRAINT; Schema: public; Owner: alexey
--

ALTER TABLE ONLY "musicTable"
    ADD CONSTRAINT "musicTable_pkey" PRIMARY KEY (id);


--
-- Name: music music_pkey; Type: CONSTRAINT; Schema: public; Owner: alexey
--

ALTER TABLE ONLY music
    ADD CONSTRAINT music_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

