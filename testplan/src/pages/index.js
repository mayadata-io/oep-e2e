import React from 'react';
import classnames from 'classnames';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './styles.module.css';

const features = [
  {
    title: <>E2E Test coverage</>,
    imageUrl: 'img/undraw_docusaurus_mountain.svg',
    description: (
      <>
	E2E covers both instantaneous testing in pipelines and soak testing on test beds that are running for a long time. Coverage refers to the percentage of test cases that are implemented against the test plan.
      </>
    ),
  },
  {
    title: <>Our persona is the Kubernetes SRE</>,
    imageUrl: 'img/undraw_docusaurus_tree.svg',
    description: (
      <>
	Kubera converts Kuberentes into a Data layer. Using Kubera, the Kubernetes SRE can increase the agility of DevOps, solve the issues around stateful applications.
      </>
    ),
  },
  {
    title: <>E2E Testing </>,
    imageUrl: 'img/undraw_docusaurus_react.svg',
    description: (
      <>
	E2E Testing should cover all aspects of product quality from the end user perspective. As they say - "In God we trust, for everything else WE TEST!"
      </>
    ),
  },
];

function Feature({imageUrl, title, description}) {
  const imgUrl = useBaseUrl(imageUrl);
  return (
    <div className={classnames('col col--4', styles.feature)}>
      {imgUrl && (
        <div className="text--center">
          <img className={styles.featureImage} src={imgUrl} alt={title} />
        </div>
      )}
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
}

function Home() {
  const context = useDocusaurusContext();
  const {siteConfig = {}} = context;
  return (
    <Layout
      title={`MayaData Kubera E2E Testing`}
      description="Description will go into a meta tag in <head />">
      <header className={classnames('hero hero--primary', styles.heroBanner)}>
        <div className="container">
          <h1 className="hero__title">{siteConfig.title} Testing</h1>
          <p className="hero__subtitle">{siteConfig.tagline}</p>
          <div className={styles.buttons}>
            <Link
              className={classnames(
                'button button--outline button--secondary button--lg',
                styles.getStarted,
              )}
                href="https://oep-pipelines.mayadata.io"
              >
              E2E Pipelines
            </Link>
          </div>
          <p></p>
          <div className={styles.buttons}>
            <Link
              className={classnames(
                'button button--outline button--secondary button--lg',
                styles.getStarted,
              )}
              to={useBaseUrl('docs/getstarted')}
              >
              Read the test plan 
            </Link>
          </div>
        </div>
      </header>
      <main>
        {features && features.length && (
          <section className={styles.features}>
            <div className="container">
              <div className="row">
                {features.map((props, idx) => (
                  <Feature key={idx} {...props} />
                ))}
              </div>
            </div>
          </section>
        )}
      </main>
    </Layout>
  );
}

export default Home;
