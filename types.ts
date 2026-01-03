
import React from 'react';

export enum AppView {
  DASHBOARD = 'DASHBOARD',
  TEMPLATES = 'TEMPLATES',
  DOCUMENTATION = 'DOCUMENTATION',
  CONTRIBUTE = 'CONTRIBUTE',
  AI_ASSISTANT = 'AI_ASSISTANT',
  DEPLOY = 'DEPLOY'
}

export interface Template {
  id: string;
  name: string;
  description: string;
  category: 'SaaS' | 'Landing' | 'E-commerce' | 'Portfolio';
  image: string;
  features: string[];
}

export interface NavItem {
  id: AppView;
  label: string;
  icon: React.ReactNode;
}
